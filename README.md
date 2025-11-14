# Higher-Ed Analytics Portfolio (Synthetic)

All datasets are **synthetic** and anonymized. This repo showcases survey analytics, data cleaning, reporting automation, and SPSS recode workflows.

## Highlights for reviewers
- **Satisfaction map:** `01-student-satisfaction-toolkit/outputs/fig_importance_vs_satisfaction.png`
- **Cohort Likerts:** `02-microsurvey-pulse/outputs/fig_likert_by_cohort.png`
- **Cleaned employers CSV:** `03-employer-cleaning/outputs/employers_clean.csv`
- **Auto report (Markdown):** `04-reporting-automation/outputs/report.md`
- **SPSS snippet:** `05-spss-syntax/recode_goals.sps`

## Project map
1. `01-student-satisfaction-toolkit` — 500 synthetic responses, 12 items (1–7). Item/scale summaries + visuals.  
2. `02-microsurvey-pulse` — 300 synthetic responses, 3 Likert items + 0–10 recommendation.  
3. `03-employer-cleaning` — string normalization → canonical employer names.  
4. `04-reporting-automation` — composes a weekly highlights report from #1 and #2.  
5. `05-spss-syntax` — reusable `.sps` recode examples.

## Run locally
```bash
python 01-student-satisfaction-toolkit/src/sps_analysis.py
python 02-microsurvey-pulse/src/analyze_micro.py
python 03-employer-cleaning/src/clean_employers.py
python 04-reporting-automation/src/generate_report.py
