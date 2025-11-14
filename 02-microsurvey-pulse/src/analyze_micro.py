#!/usr/bin/env python3
import pandas as pd

df = pd.read_csv('data/microsurvey_responses.csv')
likert_cols = ['q_helpfulness','q_communication','q_resources']
summary = df.groupby('cohort')[likert_cols].mean().round(2)
summary.to_csv('outputs/cohort_likert_means.csv')

promoters = (df['recommendation']>=9).mean()
detractors = (df['recommendation']<=6).mean()
nps = (promoters - detractors)*100
with open('outputs/nps_summary.txt','w') as f:
    f.write(f'NPS-like score: {nps:.1f}\n')
