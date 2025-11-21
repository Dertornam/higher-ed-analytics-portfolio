---
layout: default
title: Higher-ed correlation matrix
---

# Correlation matrix

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

## Interpretation

The correlation matrix shows three clear clusters of relationships: academic performance, student sentiment, and retention.

Term GPA and cumulative GPA move almost in lockstep (r ≈ 0.94), which tells us that how a student is doing this term is very similar to their overall academic history. Credits attempted and credits completed are also extremely tightly linked (r ≈ 0.94), so once students register for credits, most of them complete what they start.

Academic performance and satisfaction point in the same direction. Higher term GPA and cumulative GPA are moderately associated with higher overall satisfaction (r ≈ 0.43 and 0.40). In simple terms, students who are doing well academically tend to feel better about their experience. Age also shows a small positive relationship with GPA and satisfaction, suggesting that older students may be slightly more settled and academically successful.

Student sentiment behaves as expected. Overall satisfaction and NPS score are positively related (r ≈ 0.23), which fits the idea that satisfied students are more likely to recommend the institution. Most other links between NPS and academics or financial variables are very weak, so NPS is capturing a broader “experience” signal rather than purely academic or financial stress.

Unmet financial need tilts in the opposite direction of retention (r ≈ -0.10) and slightly in the opposite direction of NPS. This is a small effect, but it points the same way as the stories we often hear: students who feel more financially stretched are a bit less likely to come back and a bit less enthusiastic in recommending the institution.

Retention into the next term is only modestly related to any single variable. It shows small positive correlations with term GPA, cumulative GPA, and overall satisfaction (r ≈ 0.15–0.17). Think of retention as a door that opens more easily when grades and satisfaction are higher, but it is still controlled by many other unmeasured factors like life events, work, and family responsibilities.
