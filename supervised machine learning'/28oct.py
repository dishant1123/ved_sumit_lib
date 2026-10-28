# Xgboost :

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier
import matplotlib.pyplot as plt

df = pd.read_csv("supervised machine learning'/Churn_Modelling (1).csv")

# drop  : 
df =df.drop(['RowNumber','CustomerId','Surname'],axis=1)

# gender , geography converted in to numerical values  using pd.get_dummies() :
df = pd.get_dummies(df,columns=['Gender','Geography'],drop_first=True)

# check missing values :
"""
missing_values = df.isnull().sum()
print("Missing values in each column:\n", missing_values)
"""

# feature selection :
X=df.drop('Exited',axis=1)
y=df['Exited']

#train test split :
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.2,
                                                    random_state=42)

# model  
model = XGBClassifier(
    n_estimators=500,
    learning_rate=0.01,
    max_depth=5,
    criterion='logloss'
    
)

# fit  :
model.fit(X_train,y_train)

# predict :
y_predict = model.predict(X_test)   

# accuracy score :
model_accuracy=accuracy_score(y_test,y_predict)
print("Model Accuracy : ",model_accuracy)

# important features :

important =pd.Series(model.feature_importances_,index=X.columns).sort_values(ascending=False)
print("Feature Importances :\n",important)

# graph :

important.sort_values(ascending=True).plot(kind='bar',
                                           color='green',
                                           figsize=(10,6),
                                           title='Feature Importance')

plt.title('Feature Importance')
plt.show()

# test data prediction :