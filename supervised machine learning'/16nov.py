import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.metrics import accuracy_score,classification_report
from xgboost import XGBClassifier
from sklearn.ensemble import AdaBoostClassifier,GradientBoostingClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score,KFold,StratifiedKFold 
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer


"""
df = pd.read_csv("supervised machine learning'/Churn_Modelling (1).csv")

# drop  : 
df =df.drop(['RowNumber','CustomerId','Surname'],axis=1)

# gender , geography converted in to numerical values  using pd.get_dummies() :
df = pd.get_dummies(df,columns=['Gender','Geography'],drop_first=True)

# check missing values :
"""
"""missing_values = df.isnull().sum()
print("Missing values in each column:\n", missing_values)
"""
"""

# feature selection :
X=df.drop('Exited',axis=1)
y=df['Exited']

#train test split :
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.2,
                                                    random_state=42)

model =RandomForestClassifier(
    n_estimators=100,
    criterion='gini',
    random_state=42
)

model_kv =KFold(
    n_splits =5,
    shuffle=True,
    random_state=42
)

random_forest_cross =cross_val_score(
    model,
    X_train,
    y_train,
    cv=model_kv,
    scoring="accuracy"
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

# avg  accurancy : 

print("cross validation  random  forest score : ",random_forest_cross)
print("cross validation  random  forest score  avg accuracy : ",random_forest_cross.mean())
print("cross validation  random  forest score  std  deviation : ",random_forest_cross.std())
"""

# gridsearchcv : 

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
model = RandomForestClassifier(random_state=42)

# n_easti , max _deapth : 
para_grid_search ={
    "n_estimators" :[50,100,200],
    "max_depth" : [3,5,7]
} 

# gridsearch : 
grid = GridSearchCV(
    model,
    param_grid=para_grid_search,
    cv=5,
    scoring="accuracy"
)

# fit :
"""
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
"""
"""tree.plot_tree(model, 
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

grid.fit(X_train, y_train)

# predict :
y_pred = grid.predict(X_test)

# accuracy :
print("accuracy score : ", accuracy_score(y_test, y_pred))

# best model  : 

best_model =grid.best_estimator_ 
print("best model is  : ",best_model.score(X_test,y_test))

