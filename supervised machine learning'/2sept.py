"""
==>RFE (Recursive Feature Elimination):It repeatedly removes the least important feature 
until only the desired number remain.

1.regression :
2.when we use regression  : number and continuous value.
3.simple regression  : y =mx+c  
				y=predicted value 
				x=independent variable 
				m=slope :The slope tells us how much the predicted value changes when the input increases by one unit.
				c=intercept (value of y when x is 0)
4. relationship : positive ,negative 
5.cost function : how far the model's prediction are from actual value.
	ex:actual cost =70000
	   modelpredict =67000
	   loss =3000	
"""
# ex :1 
"""
ac    ac    
exp  salary  predict salary  loss
0     25000     24500         500
2     30000     29900         100
4     45000     44000         1000
6     90000     91500         +1500 

"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE

df = pd.read_csv("supervised machine learning'/customer_purchase.csv")
print(df)


Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)
IQR = Q3-Q1
print("IQR :",IQR)

upper_limit = Q3 + 1.5 * IQR
lower_limit = Q1 - 1.5 * IQR

print("upper_limit :",upper_limit)
print("lower_limit :",lower_limit)

outlier=df[(df["Salary"] < lower_limit) | (df["Salary"] > upper_limit)]
print("outlier :",outlier)

# feature engineering :
X =df[['Age','Salary','Experience']]
y=df['Purchased']

# split data set :
X_train,X_test,y_train,y_test=train_test_split(X,
                                               y,
                                               test_size=0.3, 
                                               random_state=42)

# scaler :
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(X_train)

# model selection :
model = LogisticRegression()
rfe_model = RFE(model,n_features_to_select=1)
rfe_model.fit(x_train_scaled,y_train)

# print : 

print("Selected features :\n",rfe_model.support_)