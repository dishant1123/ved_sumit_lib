import pandas as pd 
import numpy as np 
from sklearn.preprocessing import StandardScaler 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score,classification_report 
from sklearn.svm import SVC 

"""data = {
    "Age": [
        22, 25, 28, 30, 32,
        35, 38, 40, 42, 45,
        48, 50, 52, 55, 58
    ],
    "Salary": [
        25000, 30000, 35000, 40000, 45000,
        50000, 55000, 60000, 65000, 70000,
       75000, 80000, 85000, 90000, 95000
    ],
    "Purchased": [
        0, 0, 0, 0, 0,
        0, 1, 1, 1, 1,
        1, 1, 1, 1, 1
    ]
}
df =pd.DataFrame(data)

X=df[['Age','Salary']]
y=df['Purchased']

# split  : 

#train test split :
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.3,
                                                    random_state=42)

# model  
model = SVC(kernel='rbf',
            random_state=42
            )


# fit  :
model.fit(X_train,y_train)

# predict :
y_predict = model.predict(X_test)   

# accuracy score :
model_accuracy=accuracy_score(y_test,y_predict)
print("Model Accuracy : ",model_accuracy)


"""

# another dataset : bank  

df = pd.read_csv("supervised machine learning'/Churn_Modelling (1).csv")

# drop  : 
df =df.drop(['RowNumber','CustomerId','Surname'],axis=1)

# gender , geography converted in to numerical values  using pd.get_dummies() :
df = pd.get_dummies(df,columns=['Gender','Geography'],drop_first=True)

# feature selection :
X=df.drop('Exited',axis=1)
y=df['Exited']

#train test split :
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.2,
                                                    random_state=42)

# model  
model = SVC(
    kernel='linear',
    random_state=42
)


# fit  :
model.fit(X_train,y_train)

# predict :
y_predict = model.predict(X_test)   

# accuracy score :
model_accuracy=accuracy_score(y_test,y_predict)
print("Model Accuracy : ",model_accuracy)

