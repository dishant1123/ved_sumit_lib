"""
simple regression  : y =mx+c  
				y=predicted value 
				x=independent variable 
				m=slope :The slope tells us how much the predicted value changes when the input increases by one unit.
				c=intercept (value of y when x is 0)

"""

import  pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.preprocessing import StandardScaler,MinMaxScaler,LabelEncoder 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 

data = {
    "Hours": [1,2,3,4,5,6,7,8,9,10],
    "Score": [35,40,50,55,65,70,75,80,88,95]
}

df = pd.DataFrame(data)
print(df)

# plot : 
"""
plt.plot(df["Hours"],df['Score'],marker='o',linewidth=2)
plt.title("regression  graph")
plt.xlabel("Hours")
plt.ylabel("Score")
plt.show()
"""

# feature engineering :

X=df[['Hours']]
y=df['Score']

# split : 
X_train,X_test,y_train,y_test=train_test_split(X,
                                               y,
                                               test_size=0.2,
                                               random_state=42)

# model selection:
model = LinearRegression()
model.fit(X_train,y_train)

# predict :
y_predict = model.predict(X_test)
print("y_predict :",y_predict)

# intercept , slope :
print("intercept :",model.intercept_)
print("slope :",model.coef_)

# evaluate : MSE ,MAE,RMSE 
"""
hrs   marks   predict marks   loss 
1     35          34
2     40          39
3     50          49
4     55          54
5     65          64
6     70          75 
7     75          74
8     80          79
9     88          87
10    95          90

"""
# new data set : 
new_data = [[4.5]]  # hrs 
model_predict = model.predict(new_data)
print("new_model_predict :",model_predict)

# actual ,linear regression  graph :

plt.scatter(X,y,marker='o',color='red',label="actual")

plt.plot(X,
         model.predict(X),
         color='blue',
         label="linear regression")

plt.title("linear regression  graph")
plt.xlabel("Hours")
plt.ylabel("Score")
plt.grid(True)
plt.show()

"""
| Advertising Spend (₹'000) | Sales (₹'000) |
| ------------------------: | ------------: |
|                        10 |            25 |
|                        20 |            32 |
|                        30 |            40 |
|                        40 |            48 |
|                        50 |            55 |
|                        60 |            65 |
|                        70 |            72 |
|                        80 |            85 |


"""
