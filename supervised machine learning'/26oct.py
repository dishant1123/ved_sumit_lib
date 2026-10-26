import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_breast_cancer
from sklearn import tree
import matplotlib.pyplot as plt

"""data = load_breast_cancer()

print(data.feature_names)
print(data.target_names)
# print(data.DESCR)

X=data.data 
y=data.target

# split : 

X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y, 
                                                    test_size=0.3 
                                                    )

# model : 
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=4,
    random_state=42,
    min_samples_split=2,
    criterion='gini'
)

# fit :
model.fit(X_train, y_train)

# predict :
y_pred = model.predict(X_test)

# accuracy :
print("accuracy score : ", accuracy_score(y_test, y_pred))

# importance feature :
importance = model.feature_importances_
print("feature importance : ", importance)

# plot : 
plt.figure(figsize=(10,10))

tree.plot_tree(
               model.estimators_[1], 
               filled=True, 
               impurity=False,
               feature_names=data.feature_names,
               class_names=data.target_names,
               fontsize=8
               
               )
plt.title("Decision Tree")
plt.tight_layout()
plt.show()
"""

# titanic : 

df =pd.read_csv("supervised machine learning'/Titanic-Dataset_2.csv")

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

# model : 
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=4,
    random_state=42
    
)
# model fit :
model.fit(X_train,y_train)

# predict :
y_predict = model.predict(X_test)
print("predicted survived :",y_predict)

# accuracy :
Accuracy_score = accuracy_score(y_test,y_predict)
print("accuracy :",f"{Accuracy_score*100:.2f}%")

plt.figure(figsize=(10,10))

tree.plot_tree(
               model.estimators_[0], 
               filled=True, 
               impurity=False,
               feature_names=['Age','Sex','Fare','Pclass'],
               class_names=['survived','not survived'],
               fontsize=8
               
               )
plt.title("Decision Tree")
plt.tight_layout()
plt.show()
