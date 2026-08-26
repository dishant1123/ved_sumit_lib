#pip install scikit-learn

"""
example of   : split : -----> train test split 
from sklearn.model_selection import train_test_split

explain x_train,y_train,x_test,y_test -----> also using workflow 

============================================================================

ex :2 using  customer.csv  

step :1 read data set 
step :2 understand the  data  using  pandas method  like  describe  ,info
step :3 check the  missing  value  ,fill missing value
step :4  now model  can't understand the text so we use  the  encoding  method . 
        from sklearn.preprocessing import LabelEncoder
        column use : gender,purchase 

        one hot encoding : use pd.get_dummies() -----> use  city column 
step:5  concate with ,and drop  ----> city  ----> axis =1 


"""

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# ex :1 train test split  -----> using student_marks.csv
'''
df = pd.read_csv("student_marks.csv")  # student_marks.csv
# print(df.head())

# understanding : 

"""print(df.info())
print(df.describe())
"""

# features selection:
X=df[['StudyHours']]
y=df['Marks']

# split data set :

X_train,X_test,y_train,y_test=train_test_split(X,
                                               y,
                                               test_size=0.2,  # 20 test  80 train 
                                               random_state=42)

"""
X_train -----> study hrs  
y_train  -----> marks 

X_test  ----->
y_test  ----->

"""
print("X_train is :\n",X_train)
print("y_train is :\n",y_train)

print("X_test is :\n",X_test)
print("y_test is :\n",y_test)
'''

# ex : 2 using customer.csv

df = pd.read_csv("customer_data (1).csv")

# print(df)

# print(df.info())
# print(df.describe())

# print(df.isnull().sum())


df['Age'] =df['Age'].fillna(df['Age'].mean())
df['Salary']=df['Salary'].fillna(df['Salary'].median())
df['City'] =df['City'].fillna(df['City'].mode()[0]) 
df['Purchased'] =df['Purchased'].fillna(df['Purchased'].mode()[0])  
df['Education'] =df['Education'].fillna(df['Education'].mode()[0])

"""
0  ahm  3 
1  sur  2
2  raj  1    ------> 3 2 1 
"""
"""print(df.isnull().sum())
print(df)
"""
label_encoder = LabelEncoder()
df['Gender'] =label_encoder.fit_transform(df['Gender'])
df['Purchased'] =label_encoder.fit_transform(df['Purchased'])


# oridinal encoding :

education_type ={"Graduate":1,"Post Graduate":2 ,"PhD":3}
df['Education'] =df['Education'].map(education_type)
print(df)

#  hw :one  hot encoding : pd.get_dummies()

"""
Dataset
                |
        Separate X and y
                |
        ┌───────┴───────┐
        ↓               ↓
    Features          Label
       X                y
        |               |
        └───────┬───────┘
                ↓
        train_test_split()
                |
        ┌───────┴───────┐
        ↓               ↓
     Training          Testing
        |               |
     X_train          X_test
     y_train          y_test
        |               |
        ↓               ↓
   Train Model      Make Predictions
                        |
                        ↓
                   Compare with
                     y_test
                        |
                        ↓
                    Accuracy
"""
