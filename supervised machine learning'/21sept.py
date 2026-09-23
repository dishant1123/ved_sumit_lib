# poly regression  : 

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
data = pd.DataFrame({
    "Temperature":np.array([15,18,20,22,25,28,30,32,35]),
    "Sales" : np.array([100,130,160,200,270,350,420,500,650])
})

print(data)

# graph scatter plot  +  line plot :

"""
plt.figure(figsize=(10,10))

plt.plot(data['Temperature'],data['Sales'])
plt.title("Scatter Plot  --->  Temperature vs Sales")
plt.xlabel("Temperature")
plt.ylabel("Sales")
plt.show()
"""

# features selection  :
X=data[['Temperature']]
y=data['Sales']

# split data : 
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# model  :
model = LinearRegression()
model.fit(X_train,y_train)

# predict :
y_predict = model.predict(X_test)
print("predicted sales :",y_predict)

# comparsion actual vs predicted :
result = pd.DataFrame({
    'Actual':y_test.values,
    'Predicted':y_predict
})
# r2 score : 
R2_score = r2_score(y_test,y_predict)
print("R2 score :",R2_score)

# polynomial features  :
ploy = PolynomialFeatures(degree=2)
X_ploy = ploy.fit_transform(X)

# model : 
poly_model = LinearRegression()
poly_model.fit(X_ploy,y)

# predict :
y_predict_poly = poly_model.predict(X_ploy)
print("predicted sales :",y_predict_poly)

# r2 score  : 
R2_score_poly = r2_score(y,y_predict_poly)
print("R2 score :",R2_score_poly)


"""
# comparsion actual vs predicted :
result1 = pd.DataFrame({
    'Actual':y_test.values,
    'Predicted':y_predict_poly
})

print("polynomial features :",result1.head())
"""
if R2_score < R2_score_poly:
    print("\nPolynomial Regression performs better because the relationship between Temp and sales  is nonlinear.")
else:
    print("\nLinear Regression performs better.")


"""
task :1 regression  vs  poly curve 
task :2 try : degree = 3,4,6 
task :3 conclusion :
"""