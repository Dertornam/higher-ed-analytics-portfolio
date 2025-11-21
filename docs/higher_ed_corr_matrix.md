---
layout: default
title: Higher-ed correlation matrix
---

# Correlation Matrix

<div style='max-width:100%; overflow-x:auto; padding:6px; border:1px solid #e5e7eb; border-radius:8px;'>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>credits_attempted</th>
      <th>credits_completed</th>
      <th>gpa_term</th>
      <th>cum_gpa</th>
      <th>satisfaction_overall</th>
      <th>nps_score</th>
      <th>unmet_need</th>
      <th>retention_next_term</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>age</th>
      <td>1.000</td>
      <td>0.007</td>
      <td>-0.003</td>
      <td>0.217</td>
      <td>0.213</td>
      <td>0.105</td>
      <td>-0.005</td>
      <td>0.018</td>
      <td>0.063</td>
    </tr>
    <tr>
      <th>credits_attempted</th>
      <td>0.007</td>
      <td>1.000</td>
      <td>0.943</td>
      <td>-0.023</td>
      <td>-0.019</td>
      <td>0.003</td>
      <td>0.004</td>
      <td>-0.012</td>
      <td>0.006</td>
    </tr>
    <tr>
      <th>credits_completed</th>
      <td>-0.003</td>
      <td>0.943</td>
      <td>1.000</td>
      <td>-0.008</td>
      <td>-0.006</td>
      <td>0.010</td>
      <td>0.001</td>
      <td>-0.014</td>
      <td>0.009</td>
    </tr>
    <tr>
      <th>gpa_term</th>
      <td>0.217</td>
      <td>-0.023</td>
      <td>-0.008</td>
      <td>1.000</td>
      <td>0.935</td>
      <td>0.430</td>
      <td>0.055</td>
      <td>-0.002</td>
      <td>0.166</td>
    </tr>
    <tr>
      <th>cum_gpa</th>
      <td>0.213</td>
      <td>-0.019</td>
      <td>-0.006</td>
      <td>0.935</td>
      <td>1.000</td>
      <td>0.404</td>
      <td>0.044</td>
      <td>0.007</td>
      <td>0.157</td>
    </tr>
    <tr>
      <th>satisfaction_overall</th>
      <td>0.105</td>
      <td>0.003</td>
      <td>0.010</td>
      <td>0.430</td>
      <td>0.404</td>
      <td>1.000</td>
      <td>0.226</td>
      <td>0.012</td>
      <td>0.151</td>
    </tr>
    <tr>
      <th>nps_score</th>
      <td>-0.005</td>
      <td>0.004</td>
      <td>0.001</td>
      <td>0.055</td>
      <td>0.044</td>
      <td>0.226</td>
      <td>1.000</td>
      <td>-0.054</td>
      <td>0.038</td>
    </tr>
    <tr>
      <th>unmet_need</th>
      <td>0.018</td>
      <td>-0.012</td>
      <td>-0.014</td>
      <td>-0.002</td>
      <td>0.007</td>
      <td>0.012</td>
      <td>-0.054</td>
      <td>1.000</td>
      <td>-0.104</td>
    </tr>
    <tr>
      <th>retention_next_term</th>
      <td>0.063</td>
      <td>0.006</td>
      <td>0.009</td>
      <td>0.166</td>
      <td>0.157</td>
      <td>0.151</td>
      <td>0.038</td>
      <td>-0.104</td>
      <td>1.000</td>
    </tr>
  </tbody>
</table></div>

## Interpretation — Correlation Matrix

**What stands out**
Term GPA and cumulative GPA move almost together, with a very strong positive relationship. Credits attempted and credits completed show the same pattern, which means most students complete what they sign up for. Overall satisfaction is moderately tied to both term and cumulative GPA, and it also lines up with NPS, so happier students tend to be better performers and more willing to recommend the institution. Unmet financial need has a small negative relationship with retention, while GPA and satisfaction have small positive links to coming back next term.

**What it means**
Academics and sentiment are pulling in the same direction. When students are doing well, they usually feel better about their experience and are slightly more likely to return. Retention, however, is not dominated by any single variable; it behaves more like a decision influenced by many small pushes rather than one big lever. Unmet need pulls retention down only a little on its own, but it likely combines with GPA and satisfaction to create a “tipping point” for some students, like several small weights added to one side of a scale.

**Actions**
Treat GPA, satisfaction, and NPS as a connected cluster rather than separate silos. Use them together to flag students who are academically shaky and emotionally disengaged, then layer in unmet need to prioritize outreach. Build simple dashboards or heatmaps that show these correlations by program, modality, and cohort so leaders can see where the relationships are stronger or weaker, and target tutoring, advising, and financial counseling where the patterns signal the greatest risk.
