# minmax scaler,standard scaler : 

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression

df=pd.DataFrame({
    "age" :[20,22,25,28,30,34],
    "salary" :[20000,22000,25000,30000,35000, 90000]
})

print(df) 

# outlier : 2 ----> method  -----> 1. IQR  2. z-score
Q3 = df['salary'].quantile(0.75)
Q1 = df['salary'].quantile(0.25)

IQR = Q3 - Q1
print("IQR:",IQR) 

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

print("lower_limit :",lower_limit)
print("upper_limit :",upper_limit) 

outlier=df[(df["salary"] < lower_limit) | (df["salary"] > upper_limit)]
print("outlier :",outlier)

# fill outlier :
df["salary"]=df['salary'].clip(upper=upper_limit)
print(df)

# standard scaler :

"""
id    name   age   gender  credit_score  salary   loan 

101   john   29     male     670          45000    0 
102   mary   32     female   700          40000    0 
103   peter  25     male     800          35000    1
104   anna   27     female   900          45000    1
"""

X=df[['age']]
y=df['salary']

# split data set :

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3, random_state=42)

scaler  = StandardScaler()
x_train_scaled = scaler.fit_transform(X_train)
x_test_scaled = scaler.transform(X_test)

# diff : fit_transform() and transform()
"""
areasq    age    bedrooms    price 
1000       10     2            600000
2000       15     3            10000000
3000       30     4            30000000 
4000       40     5            100000000


"""

model = LinearRegression()
model.fit(x_train_scaled,y_train)
