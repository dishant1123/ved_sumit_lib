"""
1. MSE : mean Square error 
2. RMSE :root mean  Square error 
3. MAE : mean  absoulte  error 
4. R2 score 

ex : 

actual       predicted 

3               2.5 
5               4.0
7               6.5
9               8.0
11              10.5

step :1 calculate the mean of actual values : 

y^ = 3+5+7+9+11 / 5 =====>7  

step :2 calculate  the  ss_total  : 

y     y-y^    (y-y^)2
3     -4       16  
5     -2       4 
7      0       0
9      2       4 
11     4       16 
             ======
            ss_total = 40 

step :3  calculate  the  ss_residual  :

actual       predicted    error   error^2

3               2.5        0.5      0.25
5               4.0        1.0      1
7               6.5        0.5      0.25
9               8.0        1.0      1
11              10.5       0.5      0.25
                                    ======
                                    ss_residual =2.75 


apply formula  of r2 score : 

R² = 1 − (SS_Residual / SS_Total)
    = 1 - (2.75 / 40)
    =0.93 
    
the  regression model explain appox 93.13 % of the  variance in the  target variable.
"""

import  pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
import matplotlib.pyplot as plt

df = pd.read_csv("supervised machine learning'/house_price.csv")
print(df)

#scatter plot  : 

"""plt.figure(figsize=(10,10))
plt.scatter(
    df['Area'],
    df['Price']
)
plt.title("Scatter Plot  --->  Area vs Price")
plt.xlabel("Area")
plt.ylabel("Price")
plt.show()
"""

# features selection  :
X=df[["Area","Bedrooms","Age"]]
y=df['Price']

# split data :
X_train, X_test, y_train, y_test = train_test_split(X,
                                               y,
                                               test_size=0.2,
                                               random_state=42)

# model : 
model=LinearRegression()

# train/ fit model :
model.fit(X_train,y_train)

# slop , intercept  :

print("model slope :",model.coef_)
print("model intercept :",model.intercept_)

# prediction : 
y_predict =model.predict(X_test)
print("predicted price :",model.predict(X_test))

# comparsion actual vs predicted :

result = pd.DataFrame({
    'Actual':y_test.values,
    'Predicted':y_predict
})
print(result)

# evaluation :
R2_score = r2_score(y_test,y_predict)
print("R2 score :",R2_score)

MEAN_SQ_error = mean_squared_error(y_test,y_predict)
print("Mean Squared error :",MEAN_SQ_error)

MEAN_ae_error = mean_absolute_error(y_test,y_predict)
print("Mean Absolute error :",MEAN_ae_error)

Root_MEAN_SQ_error = np.sqrt(MEAN_SQ_error)
print("Root Mean Squared error :",Root_MEAN_SQ_error)

# predict new data  : 

# check  overfitting   or  underfitting  :
"""
overfitting  :  train -----> best  test ---> poor  
underfitting :  train -----> poor  test ---> poor 

"""
# r2_score : 

train_r2_score = model.score(X_train,y_train)   # train ----> 80 % area , bedrooms age ,80 % price  
test_r2_score = model.score(X_test,y_test)     # test  ---->20 %

print("train_r2_score :",train_r2_score)  
print("test_r2_score :",test_r2_score)

# difference between train and test :

diff_train_test = train_r2_score - test_r2_score
print("diff_train_test :",diff_train_test)

# check  overfitting   or  underfitting  :

if train_r2_score < 0.70  and  test_r2_score < 0.70 :
    print("model is underfitting")

elif train_r2_score- test_r2_score > 0.10 :
    print("model is overfitting")
else :
    print("model is good")


