"""
multiple linear regression :1 continuous dependent variable  using two or more independent variable.

	y =b0 +b1x1+b2x2 +....+bnxn  

y =depe , x1x2 = indepe ,b0= intercept  ,b1b2 =coefficients 

========================================
interpretations  of  coeff :

| Feature  | Coefficient |
| -------- | ----------- |
| Area     | 150         |
| Bedrooms | 12000       |
| Age      | -2500       |

Area = 150
1000 sqft
↓
1001 sqft
Price increases by ₹150

Bedrooms = 12000
Every additional bedroom increases price by ₹12,000, assuming Area and Age remain constant.

2 Bedrooms
↓
3 Bedrooms

Price increases by ₹12,000

Age = -2500
Every additional year decreases price by ₹2,500.
House Age = 10
↓
House Age = 11
Price decreases by ₹2,500

============================================

multicollinearity :two or more indep variable highly correlated with each other. 
ex: area ----> number  of rooms ----> window 
means if rooms  inc then it more window 

prlm :
Make coefficients unstable
Change coefficient values significantly with small data changes
Make feature interpretation unreliable
Reduce trust in the model

==============================================
pip install statsmodels  
from statsmodels.stats.outliers_influence import variance_inflation_factor 

detecting multicollineartiy using VIF :variance inflation factor

VIF (Variance Inflation Factor) measures how much the variance of a coefficient is increased because of multicollinearity.

VIF stands for Variance Inflation Factor.
It measures how strongly one independent variable is correlated with the other independent variables.
area  ----> bedroom , age 
bedrrom ---> area ,age 
age  ---> bedroom , area 

Remember:VIF does not compare a feature with the target (Price).
ex : 
VIF checks relationships like:

Area  <------> Bedrooms
Area  <------> Age
Bedrooms <------> Age

It does not check:
Area ------> Price

| VIF Value | Meaning                                                            |
| --------- | ------------------------------------------------------------------ |
| 1         | No correlation                                                     |
| 1 -5      | Acceptable                                                         |
| 5 - 10    | High correlation (investigate)                                     |
| >10       | Severe multicollinearity (consider removing or combining features) |

# :
No — VIF does not give regression coefficients.
It gives a diagnostic score for each predictor, telling you how much the variance of its estimated coefficient is inflated due to correlation with other predictors.

Coefficients (𝛽) come from regression formulas.

VIF is a post-analysis metric to check if those coefficients are trustworthy.


"""


# vif pratical  : 