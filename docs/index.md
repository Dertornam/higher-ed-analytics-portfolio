---
layout: default
title: Higher-Ed Analytics Portfolio
---

<style>
:root { --bg:#0f172a; --card:#0b1220; --text:#e5e7eb; --muted:#94a3b8; --accent1:#22d3ee; --accent2:#34d399; }
.hero { padding:2.5rem 1rem; background: linear-gradient(135deg, var(--accent1), var(--accent2));
  color:#0b1220; border-radius:12px; text-align:center; margin-bottom:1.5rem; }
.hero h1{ margin:0 0 .25rem 0; font-size:2.0rem; }
.btn-row{ margin-top:1rem; display:inline-flex; gap:.75rem; flex-wrap:wrap; }
.btn{ display:inline-block; padding:.6rem 1rem; border-radius:999px; text-decoration:none; font-weight:600; }
.btn.primary{ background:#0b1220; color:#e5e7eb; }
.btn.ghost{ border:2px solid #0b1220; color:#0b1220; }
.grid{ display:grid; gap:1rem; } @media(min-width:900px){ .grid.cols-2{ grid-template-columns:1fr 1fr; } }
.card{ background:var(--card); color:var(--text); border-radius:12px; padding:1rem; box-shadow:0 2px 12px rgba(0,0,0,.4); }
.caption, figcaption{ color:var(--muted); }
figure{ margin:0; } figure img{ width:100%; border-radius:10px; }
.card:hover{ box-shadow:0 8px 30px rgba(0,0,0,.55); transform:translateY(-1px); transition:.18s; }
footer.small{ margin-top:1.5rem; font-size:.9rem; color:var(--muted); }
</style>

<div class="hero">
  <h1>Turning Higher-Ed Data into Actionable Insights</h1>
  <p>From messy sources to clear decisions—cleaning, analysis, and automated reporting.</p>
  <div class="btn-row">
    <a class="btn primary" href="#work">Explore My Projects</a>
    <a class="btn ghost" href="https://github.com/{{ site.github.owner_name }}/{{ site.github.repository_name }}">View on GitHub</a>
    <a class="btn ghost" href="./resume.pdf">Download Résumé</a>
  </div>
  <div class="kpis" style="margin-top:1rem;">
    <div class="kpi">RNL PSOL multi-year analysis</div>
    <div class="kpi">SPSS + Python reproducibility</div>
    <div class="kpi">Auto weekly Markdown reports</div>
  </div>
</div>

## Overview
Imagine messy student surveys and employer lists transformed into decisions leaders can act on.
This portfolio shows how I clean, analyze, and visualize higher-ed data—fast and repeatably.

**Process**: Raw Data → Cleaning → Analysis → Visualization → Insights

---

## Why Higher-Ed Analytics?
- Improve student satisfaction, retention, and time-to-degree.  
- Support accreditation/IPEDS reporting with trustworthy pipelines.  
- Give leaders tight, visual summaries they can use in minutes.

---

## Featured visuals {#work}

<div class="grid cols-2">
  <div class="card">
    <figure>
      <img src="./fig_1.png" alt="Importance vs Satisfaction map">
      <figcaption><strong>Satisfaction Map.</strong> Prioritizes gaps between importance and satisfaction to guide resource allocation.</figcaption>
    </figure>
  </div>
  <div class="card">
    <figure>
      <img src="./fig_2.png" alt="Cohort Likert comparisons">
      <figcaption><strong>Cohort Likerts.</strong> Compares item-level satisfaction across student groups to target interventions.</figcaption>
    </figure>
  </div>
</div>

<p class="caption">
See also: <a href="./report.md">Weekly Insights (Markdown)</a> · <a href="./cleaned.csv">Cleaned employers CSV</a>
</p>

---

## Mini case study: Data-informed improvement
**Challenge:** Identify the levers behind student satisfaction and convert findings into an executive brief.  
**Approach:** Merged multi-year RNL PSOL responses; built SPSS syntax for recodes; used Python for charts and an automated Markdown report; framed actions with Improvement Science (PDSA).  
**Impact:** Clear, prioritized actions for program leads; reproducible pipeline for semester refreshes.

---

## Statistical analysis

- **Descriptive statistics:** [CSV]({{ '/desc_stats.csv' | relative_url }})
- **Correlation matrix:** [CSV]({{ '/corr_matrix.csv' | relative_url }}) ·
  [Heatmap]({{ '/corr_heatmap.png' | relative_url }})
- **Regression (OLS):** [Results]({{ '/regression_results.md' | relative_url }})

*Runs on anonymized datasets and refreshes via GitHub Actions.*
---

## Skills & Tools
<div class="badges">
  <span>SPSS</span> <span>Python</span> <span>Pandas</span> <span>Matplotlib</span>
  <span>Tableau</span> <span>SQL</span> <span>Markdown automation</span>
  <span>GitHub Actions</span> <span>Data governance & policy</span>
</div>

---

## What I bring to your team
- Data cleaning & reproducibility across SPSS and Python.  
- Survey analytics expertise (Likerts, gap analysis, cohort comparisons).  
- Automated reporting workflows that keep leaders updated weekly.  
- Improvement Science (PDSA) framing to turn insights into practice.

<footer class="small">
  All datasets shown here are anonymized.
</footer>
