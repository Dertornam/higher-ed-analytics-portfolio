---
layout: default
title: Higher-Ed Analytics Portfolio
---

# Overview
Results-focused samples for institutional research and analytics. The goal is to show how I move from messy inputs to clear decisions—fast and reproducibly.

**Live repo:** https://github.com/Dertornam/higher-ed-analytics-portfolio  
**Download ZIP:** https://github.com/Dertornam/higher-ed-analytics-portfolio/archive/refs/heads/main.zip

---

## What’s inside (at a glance)
- **Student Satisfaction Toolkit** — 500 synthetic responses, 12 items (1–7). Item/scale summaries, gaps, and visuals.  
- **Micro-Survey Pulse** — 300 responses, 3 Likert items + 0–10 recommendation. Cohort comparisons + NPS-style score.  
- **Employer Cleaning** — string normalization → canonical employer names (no external deps).  
- **Reporting Automation** — composes a weekly Markdown highlights report from the two surveys.  
- **SPSS Syntax** — reusable `.sps` snippets for common recodes.

---

## Featured visuals
- **Satisfaction map**  
  ![Importance vs Satisfaction](https://raw.githubusercontent.com/Dertornam/higher-ed-analytics-portfolio/main/01-student-satisfaction-toolkit/outputs/fig_importance_vs_satisfaction.png)

- **Cohort Likerts**  
  ![Likert by Cohort](https://raw.githubusercontent.com/Dertornam/higher-ed-analytics-portfolio/main/02-microsurvey-pulse/outputs/fig_likert_by_cohort.png)

---

## Artifacts (open in browser)
- **Weekly Insights (Markdown):**  
  https://raw.githubusercontent.com/Dertornam/higher-ed-analytics-portfolio/main/04-reporting-automation/outputs/report.md  
- **Cleaned employers (CSV):**  
  https://raw.githubusercontent.com/Dertornam/higher-ed-analytics-portfolio/main/03-employer-cleaning/outputs/employers_clean.csv

---

## How to run locally
```bash
python 01-student-satisfaction-toolkit/src/sps_analysis.py
python 02-microsurvey-pulse/src/analyze_micro.py
python 03-employer-cleaning/src/clean_employers.py
python 04-reporting-automation/src/generate_report.py
