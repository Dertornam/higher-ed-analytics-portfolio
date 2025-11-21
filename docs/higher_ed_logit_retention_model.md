# Logistic regression: next-term retention


<pre>
                            Logit Regression Results                           
===============================================================================
Dep. Variable:     retention_next_term   No. Observations:                 1500
Model:                           Logit   Df Residuals:                     1495
Method:                            MLE   Df Model:                            4
Date:                 Thu, 20 Nov 2025   Pseudo R-squ.:                 0.04021
Time:                         20:23:04   Log-Likelihood:                -924.79
converged:                        True   LL-Null:                       -963.53
Covariance Type:             nonrobust   LLR p-value:                 5.954e-16
=====================================================================================================
                                        coef    std err          z      P&gt;|z|      [0.025      0.975]
-----------------------------------------------------------------------------------------------------
Intercept                            -3.3102      0.572     -5.790      0.000      -4.431      -2.190
C(program_level)[T.Undergraduate]    -0.3043      0.125     -2.432      0.015      -0.549      -0.059
gpa_term                              0.5807      0.165      3.513      0.000       0.257       0.905
satisfaction_overall                  0.4875      0.139      3.498      0.000       0.214       0.761
unmet_need                           -0.0001   3.46e-05     -4.186      0.000      -0.000    -7.7e-05
=====================================================================================================
</pre>

## Interpretation — Logistic regression (next-term retention)

**What the model says (plain English).**  
Students with higher term GPA and higher overall satisfaction have greater odds of returning next term. Undergraduates have lower odds of retention than graduate students, even after controlling for GPA and satisfaction. As unmet financial need increases, the odds of coming back decline, although each dollar has a small effect on its own.

**What it means for advising and enrollment.**  
Persistence is not driven by a single factor. Academic performance, student experience, and financial strain all push in consistent directions. A student who is struggling academically, feels less satisfied, and carries high unmet need sits in a much more fragile zone than the coefficients suggest when viewed one at a time.

**Actions.**  
Use this model to flag at-risk students in a retention dashboard. Prioritize outreach to undergraduates who combine lower GPA, lower satisfaction, and higher unmet need. Pair academic interventions with targeted financial counseling and service improvements so that support touches both the academic and financial sides of the student experience at the same time.
