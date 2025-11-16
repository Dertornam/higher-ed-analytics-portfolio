# OLS Regression — outcome: `recommendation`

- N = 300  |  k = 3 predictors

## Top coefficients

|                 |       coef |         t |        p |
|:----------------|-----------:|----------:|---------:|
| q_helpfulness   | -0.195008  | -1.55331  | 0.121417 |
| q_resources     |  0.0624333 |  0.487811 | 0.626045 |
| q_communication | -0.023873  | -0.190269 | 0.849229 |

## Full summary
```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:         recommendation   R-squared:                       0.009
Model:                            OLS   Adj. R-squared:                 -0.001
Method:                 Least Squares   F-statistic:                    0.9144
Date:                Sun, 16 Nov 2025   Prob (F-statistic):              0.434
Time:                        01:34:58   Log-Likelihood:                -764.31
No. Observations:                 300   AIC:                             1537.
Df Residuals:                     296   BIC:                             1551.
Df Model:                           3                                         
Covariance Type:            nonrobust                                         
===================================================================================
                      coef    std err          t      P>|t|      [0.025      0.975]
-----------------------------------------------------------------------------------
const               5.3150      0.738      7.201      0.000       3.862       6.768
q_helpfulness      -0.1950      0.126     -1.553      0.121      -0.442       0.052
q_communication    -0.0239      0.125     -0.190      0.849      -0.271       0.223
q_resources         0.0624      0.128      0.488      0.626      -0.189       0.314
==============================================================================
Omnibus:                      105.969   Durbin-Watson:                   2.028
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               16.185
Skew:                           0.079   Prob(JB):                     0.000306
Kurtosis:                       1.873   Cond. No.                         23.3
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```