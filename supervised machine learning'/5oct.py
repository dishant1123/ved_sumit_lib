import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix,classification_report

df =pd.read_csv("supervised machine learning'/Titanic-Dataset_2.csv")
print(df.head())

# missing value :
# print(df.isnull().sum())

# age -----> fillna ----> mean , mapping -----> df[sex]
df['Age'] =df['Age'].fillna(df['Age'].mean())
df['Sex'] = df['Sex'].map({'male':0,'female':1})

# feature selection :
X = df[['Age','Sex','Fare','Pclass']]
y = df['Survived']

# split data :
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# model  : 
model = LogisticRegression(max_iter=1000)

# model fit :
model.fit(X_train,y_train)

# predict : 
y_predict = model.predict(X_test)
print("predicted survived :",y_predict)

# accuracy :
Accuracy_score = accuracy_score(y_test,y_predict)
print("accuracy :",f"{Accuracy_score*100:.2f}%")

# overfitting : 
