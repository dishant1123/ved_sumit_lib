# KNN  : k Nearest Neighbors
"""

based distance   : 

1. euclidean distance
2. manhattan distance

arg : k = number of neighbors =3

example 1: predicating movie generation  : 

| IMDb Rating              | Duration | Genre  |
| ------------------------ | -------- | ------ |
| 8.0 (Mission Impossible) | 160      | Action | 46 
| 6.2 (Gadar 2)            | 170      | Action | 56
| 7.2 (Rocky & Rani)       | 168      | Comedy | 54  
| 7.0 (OMG 2)              | 155      | Comedy | 41 

now predict the genre of  "barbie" movie with IMDB_rating 7.4 and  duration 114 

1. euclidean distance : 
d = sqrt((x1-x2)^2 + (y1 -y2)^2)

        (8 - 7.4)^2  + (160 - 114)^2   

2. manhattan distance :

d= |x1-x2| + |y1 -y2|


example 2: 

ex :2  try this   ===>  take  k=1

Query → X = (Maths = 6, CS = 8)

| Maths | CS | Result |
| ----- | -- | ------ |
| 4     | 3  | Fail   |
| 6     | 7  | Pass   |
| 7     | 8  | Pass   |
| 5     | 5  | Fail   |
| 8     | 8  | Pass   |


"""
# titanic : 

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix,classification_report
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
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
# scaler :
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# model : 
"""model = KNeighborsClassifier(n_neighbors=5,
                             metric='euclidean')

# model fit :
model.fit(X_train,y_train)

# predict :
y_predict = model.predict(X_test)
print("predicted survived :",y_predict)

# accuracy :
Accuracy_score = accuracy_score(y_test,y_predict)
print("accuracy :",f"{Accuracy_score*100:.2f}%")
"""
# new  data  predict :
"""new_data = pd.DataFrame({
   "Age" : [34],
    "Sex" :[1],
    "Fare" :[10.25],
    "Pclass" :[3]
       
})

new_data = scaler.transform(new_data)
new_data_predict = model.predict(new_data)

print("new data predicted survived :",new_data_predict)

"""
# elbow method  : 

k_value = range(1,11)  # 1,10 
accuracy_scores = []

for  i in k_value:
    model = KNeighborsClassifier(n_neighbors=i,metric='euclidean')
    model.fit(X_train,y_train)
    y_predict = model.predict(X_test)
    accuracy_scores.append(accuracy_score(y_test,y_predict)) 
    
plt.plot(k_value,accuracy_scores)
plt.xlabel('k value')
plt.ylabel('accuracy')
plt.title('Accuracy Scores')
plt.show()

