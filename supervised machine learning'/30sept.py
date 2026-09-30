# logistic regression  :

"""
step : 1 read csv file 
step : 2 missing value  ,  data  info  , describe , fillna 
step : 3 feature selection 
step : 4 train test split 
step : 5 model 
step : 6  fit ,probability,predict
step : 7 evaluate : accuracy , precision , recall , f1 score
step : 8 confusion matrix , classification report 


ex : 

id    name    marks   result 
1     john    10      fail
2     sita    34      fail
3     ravan   65      pass 
4     ram     78      pass  

"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix,classification_report
from sklearn.preprocessing import StandardScaler


df = pd.read_csv("supervised machine learning'/logistic_regression_small.csv")
print(df.head())

X=df[['Age','Salary','Experience']]
y=df['Purchased']

# split data :
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

# feature scale :
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(X_train)
x_test_scaled = scaler.transform(X_test)

# model : 
model = LogisticRegression(max_iter=1000,
                           random_state=42)
model.fit(x_train_scaled,y_train)

# predict : 
y_predict = model.predict(x_test_scaled)
print("predicted purchased :",y_predict)

# probability :
y_predict_proba = model.predict_proba(x_test_scaled)[:,1]
print("probability :",y_predict_proba)

# accuracy :
Accuracy_score = accuracy_score(y_test,y_predict)
print("accuracy :",Accuracy_score)

