from pathlib import Path
import os, re
import numpy as np, pandas as pd, matplotlib.pyplot as plt
import statsmodels.api as sm

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
(DOCS / ".").mkdir(parents=True, exist_ok=True)

def find_csv():
    p = os.getenv("SURVEY_CSV")
    if p and Path(p).exists(): return Path(p)
    # fallback: any CSV in docs/
    for c in sorted(DOCS.glob("*.csv")):
        return c
    raise FileNotFoundError("Set SURVEY_CSV to a numeric survey CSV under docs/")

def numeric_cols(df):
    cols = df.select_dtypes(include="number").columns.tolist()
    drop = [c for c in cols if re.search(r"(id|key)$", c, flags=re.I)]
    cols = [c for c in cols if c not in drop]
    if len(cols) < 2: raise ValueError("Need ≥2 numeric columns")
    return cols

def choose_y(df, cols):
    aliases = ["overall_satisfaction","overall","recommendation",
               "recommendation_score","nps","nps_score"]
    lower = {c.lower(): c for c in df.columns}
    for a in aliases:
        if a in lower: return lower[a]
    return cols[-1]

csv = find_csv()
df  = pd.read_csv(csv)
nums = numeric_cols(df)

# Descriptives
desc = df[nums].describe().T
desc.to_csv(DOCS/"desc_stats.csv")

# Correlation + heatmap
corr = df[nums].corr(numeric_only=True)
corr.to_csv(DOCS/"corr_matrix.csv")
plt.figure(figsize=(8,6))
plt.imshow(corr.values, aspect="auto"); plt.colorbar(label="Pearson r")
plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.index)), corr.index)
plt.title("Correlation Matrix"); plt.tight_layout()
plt.savefig(DOCS/"corr_heatmap.png", dpi=150); plt.close()

# OLS
y_col = choose_y(df, nums)
X_cols = [c for c in nums if c != y_col]
X = sm.add_constant(df[X_cols].fillna(df[X_cols].median()))
y = df[y_col].fillna(df[y_col].median())
model = sm.OLS(y, X).fit()

coefs = model.params.drop("const").to_frame("coef")
coefs["t"] = model.tvalues.drop("const"); coefs["p"] = model.pvalues.drop("const")
coefs = coefs.reindex(coefs["coef"].abs().sort_values(ascending=False).index)

md = []
md += [f"# OLS Regression — outcome: `{y_col}`\n",
       f"- N = {len(df)}  |  k = {len(X_cols)} predictors\n",
       "## Top coefficients\n",
       coefs.head(12).to_markdown(index=True), "\n## Full summary\n",
       "```\n"+str(model.summary())+"\n```"]
(Path(DOCS/"regression_results.md")).write_text("\n".join(md), encoding="utf-8")

print(f"OK: wrote desc_stats.csv, corr_matrix.csv, corr_heatmap.png, regression_results.md to docs/")
