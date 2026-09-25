
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
"""
for i in range(2,7):
    ploy = PolynomialFeatures(degree=i)
    X_train_ploy = ploy.fit_transform(X_train)
    X_test_ploy = ploy.transform(X_test)

    # model : 
    poly_model = LinearRegression()
    poly_model.fit(X_train_ploy,y_train)

    # predict :
    y_predict_poly = poly_model.predict(X_test_ploy)
    print("predicted sales :",y_predict_poly)

    # comparsion actual vs predicted :
    result1 = pd.DataFrame({
        'Actual':y_test.values,
        'Predicted':y_predict_poly
    })

    print("polynomial features :",result1.head())

    # r2 score :
    R2_score_poly = r2_score(y_test,y_predict_poly)
    print(f"Degree : {i} R2 score : {R2_score_poly}") 
"""

ploy = PolynomialFeatures(degree=4)
X_train_ploy = ploy.fit_transform(X_train)
X_test_ploy = ploy.transform(X_test)

# model : 
poly_model = LinearRegression()
poly_model.fit(X_train_ploy,y_train)

# predict :
y_predict_poly = poly_model.predict(X_test_ploy)
print("predicted sales :",y_predict_poly)

# comparsion actual vs predicted :
result1 = pd.DataFrame({
'Actual':y_test.values,
'Predicted':y_predict_poly
})

print("polynomial features :",result1.head())

# r2 score :
R2_score_poly = r2_score(y_test,y_predict_poly)
print("R2 score : ",R2_score_poly) 

plt.figure(figsize=(10,10))

plt.plot(X,model.predict(X),label="Linear",color="red")
plt.plot(X,poly_model.predict(ploy.transform(X)),label="Poly", color="blue")
plt.title("Linear Vs Poly")
plt.xlabel("Temparature")
plt.ylabel("Sales")
plt.show()

"""
task :1 regression  vs  poly curve 
task :2 try : degree = 3,4,6 
task :3 conclusion :
### Conclusion

1. **Linear Regression** captures the overall upward trend well ($R^2 \approx 0.98$), but it struggles to adapt to the accelerating rate of sales at higher temperatures.
2. **Polynomial Regression** ($degree = 4$) fits the non-linear curve of the data almost perfectly ($R^2 \approx 1.00$), capturing the non-linear relationship between temperature and sales.
3. **Key Coding Takeaway**: When evaluating or plotting predictions from a `PolynomialFeatures` model, raw feature inputs $X$ must always be transformed using `poly.transform(X)` before passing them into `poly_model.predict()`.
"""