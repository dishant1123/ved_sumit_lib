"""

1. data set : salary 
2. feature selection 
3. train split 
4. feature scale  :fit_transform(),transform()
5. linear model 
6. ridge 
7. lasso 
8. elasticnet 

| Alpha | Effect                                        |
| ----- | --------------------------------------------- |
| 0     | No regularization (same as Linear Regression) |
| 0.001 | Very little regularization                    |
| 0.01  | Small regularization                          |
| 0.1   | Mild regularization                           |
| 1     | Default in most examples                      |
| 10    | Strong regularization                         |
| 100   | Very strong regularization                    |
| 1000  | May cause underfitting                        |

The alpha and l1_ratio values are hyperparameters, meaning there is no fixed value. They are usually chosen by cross-validation


| Model      | Recommended Value         |
| ---------- | ------------------------- |
| Ridge      | alpha=1                 	 |
| Lasso      | alpha=0.1 or alpha=1 	 |
| ElasticNet | alpha=1, l1_ratio=0.5 	 |

"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression,Ridge,Lasso,ElasticNet
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score


df = pd.read_excel("supervised machine learning'/salary_regularization.xlsx") 

# feature selection :

X= df.drop(['Salary'],axis=1)  # df[['experience','education','age','project']]
y= df['Salary']

# split data :
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# feature scale :
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# model : 
model = LinearRegression()
model.fit(X_train_scaled,y_train)

# predict : 
y_predict = model.predict(X_test_scaled)
print("predicted salary :",y_predict)

# r2 score : 
R2_score = r2_score(y_test,y_predict)
print("R2 score :",R2_score)
