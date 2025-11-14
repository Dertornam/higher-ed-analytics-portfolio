# Student Satisfaction Toolkit (Synthetic)

An anonymized, end-to-end example of analyzing student satisfaction data using synthetic responses.

## What's here
- `data/synthetic_sps_responses.csv` — 500 synthetic records, 12 items (importance & satisfaction 1–7), plus demographics.
- `outputs/item_summary.csv` — per-item means and performance gaps, with basic strength/challenge tagging.
- `outputs/scale_summary.csv` — four illustrative scales with importance, satisfaction, and gaps.
- Visuals:
  - `fig_importance_vs_satisfaction.png`
  - `fig_scale_satisfaction.png`
  - `fig_satisfaction_by_group.png`
- `src/sps_analysis.py` — a reproducible script that recomputes these summaries and figures.

## Methods (brief)
- **Performance gap** = mean(importance) − mean(satisfaction).
- **Strengths** = items in top-half of importance and top quartile of satisfaction.
- **Challenges** = items in top-half of importance and in bottom quartile of satisfaction or top quartile of gap.

> All data are synthetic and anonymized. No real student or institutional data are included.
