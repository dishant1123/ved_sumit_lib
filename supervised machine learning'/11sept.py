import  pandas as pd  
import numpy as np 
from sklearn.preprocessing import StandardScaler 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 
from statsmodels.stats.outliers_influence import variance_inflation_factor 

# read _csv : 

df = pd.read_csv("supervised machine learning'/house_price.csv")

# feature selection  : 

X=df[["Area","Bedrooms","Age"]]
y=df['Price']

# split  : 
X_train, X_test, y_train, y_test = train_test_split(X,
                                               y,
                                               test_size=0.2,
                                               random_state=42)

# model : 
model=LinearRegression()

# model fit :
model.fit(X_train,y_train)

# predict : 
y_predict = model.predict(X_test)
print(y_predict)

# evaluation  : 

# actual vs predicted :
result  =pd.DataFrame({
    "Actual":y_test,
    "Predicted":y_predict
})
print(result.head(10))

intercept = model.intercept_
print("intercept :",intercept)

coef = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
}
)

# VIF : 

vif =pd.DataFrame()
vif['Feature']=X.columns
vif['VIF']=[
        variance_inflation_factor(X.values,i)
        for i in range(X.shape[1])
        ]
print(vif)

importance =coef.copy()
importance["Absolute"] = importance["Coefficient"].abs()

# print(importance.sort_values("Absolute",ascending=False).head())
print("\nFeature Importance")
print(
    importance.sort_values(
        by="Absolute",
        ascending=False
    )[["Feature", "Coefficient"]]
)

"""
conclusion : 

"""


