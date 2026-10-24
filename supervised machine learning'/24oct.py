"""
decision tree : classification 
data set : breast_cancer

"""
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_breast_cancer
from sklearn import tree
import matplotlib.pyplot as plt

data = load_breast_cancer()

print(data.feature_names)
print(data.target_names)
# print(data.DESCR)

X=data.data 
y=data.target

# split : 

X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y, 
                                                    test_size=0.3, 
                                                    random_state=0)

# model : 
model = DecisionTreeClassifier(
    criterion='gini',
    max_depth=4,
    random_state=42
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

tree.plot_tree(model, 
               filled=True, 
               impurity=False,
               feature_names=data.feature_names,
               class_names=data.target_names,
               fontsize=8
               
               )
plt.title("Decision Tree")
plt.tight_layout()
plt.show()