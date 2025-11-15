---
layout: default
title: Higher-Ed Analytics Portfolio
---

<style>
.hero { padding: 2.5rem 1rem; background: linear-gradient(135deg,#0ea5e9 0%, #10b981 100%);
        color: #fff; border-radius: 12px; text-align: center; margin-bottom: 1.5rem; }
.hero h1 { margin: 0 0 .25rem 0; font-size: 2.0rem; }
.btn-row { margin-top: 1rem; display: inline-flex; gap: .75rem; flex-wrap: wrap; }
.btn { display:inline-block; padding:.6rem 1rem; border-radius:999px; text-decoration:none; font-weight:600; }
.btn.primary { background:#fff; color:#0f172a; }
.btn.ghost { border:2px solid #fff; color:#fff; }
.grid { display:grid; gap:1rem; }
@media(min-width:900px){ .grid.cols-2 { grid-template-columns: 1fr 1fr; } }
.card { background:#fff; border-radius:12px; padding:1rem; box-shadow:0 2px 12px rgba(0,0,0,.06); }
.caption { font-size:.95rem; color:#475569; margin:.5rem 0 0 0; }
.kpis { display:flex; gap:1rem; flex-wrap:wrap; justify-content:center; }
.kpi { background:#ecfeff; border:1px solid #cffafe; border-radius:10px; padding:.5rem .75rem; font-weight:600; }
.badges span { display:inline-block; background:#f1f5f9; border-radius:999px; padding:.35rem .7rem; margin:.25rem; }
figure { margin:0; }
figure img { width:100%; border-radius:10px; }
figcaption { font-size:.95rem; color:#475569; margin-top:.35rem; }
footer.small { margin-top:1.5rem; font-size:.9rem; color:#64748b; }
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

## Skills & Tools
<div class="badges">
  <span>SPSS</span><span>Python</span><span>Pandas</span><span>Matplotlib</span>
  <span>Tableau</span><span>SQL</span><span>Markdown automation</span>
  <span>GitHub Actions</span><span>Data governance & policy</span>
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
