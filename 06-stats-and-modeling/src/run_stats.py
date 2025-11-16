# 06-stats-and-modeling/src/run_stats.py
from pathlib import Path
import os, re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

ROOT = Path(__file__).resolve().parents[2]
OUT  = ROOT / "06-stats-and-modeling" / "outputs"
DOCS = ROOT / "docs"
OUT.mkdir(parents=True, exist_ok=True)
DOCS.mkdir(parents=True, exist_ok=True)

def find_csv():
    # 1) explicit override
    env = os.getenv("SURVEY_CSV")
    if env and Path(env).exists(): return Path(env)

    # 2) common places in your repo
    candidates = [
        ROOT/"01-student-satisfaction-toolkit"/"data"/"student_satisfaction.csv",
        ROOT/"02-microsurvey-pulse"/"data"/"micro_pulse.csv",
        ROOT/"02-microsurvey-pulse"/"data"/"microsurvey.csv",
        ROOT/"docs"/"cleaned.csv",                # fallback: uploaded CSV in docs/
    ]
    for c in candidates:
        if c.exists(): return c

    # 3) last resort: any CSV in these folders
    for d in [ROOT/"01-student-satisfaction-toolkit"/"data",
              ROOT/"02-microsurvey-pulse"/"data",
              ROOT/"docs"]:
        if d.exists():
            for c in sorted(d.glob("*.csv")):
                return c
    raise FileNotFoundError("No CSV found. Set SURVEY_CSV to a CSV path or add one under docs/ or data/.")

def choose_outcome(df):
    # Try common outcome names; else last numeric col
    aliases = ["overall_satisfaction","overall","satisfaction_overall",
               "recommendation","recommendation_score","recommend","nps","nps_score"]
    lc = {c.lower(): c for c in df.columns}
    for a in aliases:
        if a in lc: return lc[a]
    nums = df.select_dtypes(include="number").columns.tolist()
    if not nums: raise ValueError("No numeric columns to model.")
    return nums[-1]

def numeric_cols(df):
    cols = df.select_dtypes(include="number").columns.tolist()
    drop = [c for c in cols if re.search(r"(id|key)$", c, flags=re.I)]
    return [c for c in cols if c not in drop]

csv = find_csv()
df  = pd.read_csv(csv)
nums = numeric_cols(df)
if len(nums) < 2:
    raise ValueError(f"Need ≥2 numeric columns; found {len(nums)} in {csv.name}")

# ----- Descriptives
desc = df[nums].describe().T
desc.to_csv(OUT/"desc_stats.csv")
desc.to_csv(DOCS/"desc_stats.csv")

# ----- Correlation matrix + heatmap
corr = df[nums].corr(numeric_only=True)
corr.to_csv(OUT/"corr_matrix.csv")
corr.to_csv(DOCS/"corr_matrix.csv")

plt.figure(figsize=(8,6))
plt.imshow(corr.values, aspect="auto")
plt.colorbar(label="Pearson r")
plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.index)), corr.index)
plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig(DOCS/"corr_heatmap.png", dpi=150)
plt.close()

# ----- OLS regression
y_col = choose_outcome(df)
X_cols = [c for c in nums if c != y_col]
X = sm.add_constant(df[X_cols].fillna(df[X_cols].median()))
y = df[y_col].fillna(df[y_col].median())
model = sm.OLS(y, X).fit()

md = []
md.append(f"# OLS Regression — outcome: `{y_col}`\n")
md.append(f"- N = {len(df)}  |  k = {len(X_cols)} predictors\n")
md.append("## Top coefficients\n")
coefs = model.params.drop("const").to_frame("coef")
coefs["t"] = model.tvalues.drop("const")
coefs["p"] = model.pvalues.drop("const")
coefs = coefs.reindex(coefs["coef"].abs().sort_values(ascending=False).index)
md.append(coefs.head(12).to_markdown())
md.append("\n## Full summary\n```\n"+str(model.summary())+"\n```")
(Path(DOCS/"regression_results.md")).write_text("\n".join(md), encoding="utf-8")

print(f"Done. Source={csv} → docs/: desc_stats.csv, corr_matrix.csv, corr_heatmap.png, regression_results.md")
