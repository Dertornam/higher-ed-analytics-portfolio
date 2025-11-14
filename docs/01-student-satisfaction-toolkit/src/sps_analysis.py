#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/synthetic_sps_responses.csv')
items = sorted({c.split('_')[0] for c in df.columns if c.endswith('_importance')})

rows = []
for it in items:
    imp = df[f'{it}_importance'].mean()
    sat = df[f'{it}_satisfaction'].mean()
    rows.append(dict(item=it, importance_mean=imp, satisfaction_mean=sat, gap=imp-sat))
item_summary = pd.DataFrame(rows)

imp_median = item_summary['importance_mean'].median()
sat_upper = item_summary['satisfaction_mean'].quantile(0.75)
sat_lower = item_summary['satisfaction_mean'].quantile(0.25)
gap_upper = item_summary['gap'].quantile(0.75)

def classify(r):
    if r['importance_mean'] < imp_median:
        return '—'
    if r['satisfaction_mean'] >= sat_upper:
        return 'Strength'
    if (r['satisfaction_mean'] <= sat_lower) or (r['gap'] >= gap_upper):
        return 'Challenge'
    return '—'

item_summary['classification'] = item_summary.apply(classify, axis=1)
item_summary.to_csv('outputs/item_summary.csv', index=False)

plt.figure()
plt.scatter(item_summary['importance_mean'], item_summary['satisfaction_mean'])
for _, r in item_summary.iterrows():
    plt.annotate(r['item'], (r['importance_mean'], r['satisfaction_mean']), fontsize=8, xytext=(3,3), textcoords='offset points')
plt.axvline(imp_median, linestyle='--')
plt.axhline(sat_upper, linestyle='--')
plt.axhline(sat_lower, linestyle='--')
plt.title('Items: Importance vs Satisfaction')
plt.xlabel('Mean Importance (1–7)')
plt.ylabel('Mean Satisfaction (1–7)')
plt.savefig('outputs/fig_importance_vs_satisfaction.png', bbox_inches='tight')
