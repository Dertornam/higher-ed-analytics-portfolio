#!/usr/bin/env python3
import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parent        # .../04-reporting-automation/src
PORTFOLIO = BASE.parent.parent               # .../ (root of portfolio)

sps = pd.read_csv(PORTFOLIO / '01-student-satisfaction-toolkit' / 'data' / 'synthetic_sps_responses.csv')
micro = pd.read_csv(PORTFOLIO / '02-microsurvey-pulse' / 'data' / 'microsurvey_responses.csv')

items = sorted({c.split('_')[0] for c in sps.columns if c.endswith('_importance')})
rows = []
for it in items:
    imp = sps[f'{it}_importance'].mean()
    sat = sps[f'{it}_satisfaction'].mean()
    rows.append((it, imp, sat, imp-sat))
summary = pd.DataFrame(rows, columns=['item','importance_mean','satisfaction_mean','gap']).sort_values('importance_mean', ascending=False)

top_strengths = summary.sort_values(['satisfaction_mean'], ascending=False).head(5)['item'].tolist()
top_challenges = summary.sort_values(['gap'], ascending=False).head(5)['item'].tolist()

promoters = (micro['recommendation']>=9).mean()
detractors = (micro['recommendation']<=6).mean()
nps = (promoters - detractors)*100

md = []
md.append('# Weekly Insights (Synthetic)\n')
md.append('This example shows how an automated report could summarize key metrics from surveys.\n')
md.append('## Highlights\n')
md.append(f'- *NPS-like score:* **{nps:.1f}**\n')
md.append('- *Top strengths (by satisfaction):* ' + ', '.join(top_strengths) + '\n')
md.append('- *Top challenges (by gap):* ' + ', '.join(top_challenges) + '\n')
OUTPUT = BASE.parent / 'outputs' / 'report.md'
OUTPUT.write_text('\n'.join(md), encoding='utf-8')
