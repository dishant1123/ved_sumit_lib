# missing value , fillna() ,dropna() :

import  pandas as pd
import numpy as np
"""df =pd.DataFrame({
    'name' :["saloni","ved","sumit","jay",np.nan],
    'age' :[23,29,27,np.nan,30],
    'salary' :[np.nan,50000,np.nan,np.nan,78000]
})
print(df)
"""
# missing value :
"""
print(df.isnull())
print(df.isna().sum())
"""
# missing value  drop  : 
"""
df = df.drop(axis=1,columns=['name'])
df =df.drop(axis=0,index=[0,2])   # row  , index : 0,2 

df =df.dropna(axis=0)  # drop all rows with any missing value 
df =df.dropna(axis=1)  # drop all columns with any missing value
df = df.dropna(axis=0,how='all')  # all : all value  are missing then particular row or col will remove
df =df.dropna(axis =0,thresh=1,subset=['age','salary'])  
print(df)
"""

# fill the  missing value  : 

"""
df =df.fillna(axis=1,value=0)  # fill the missing value in  age  col with 0
df['age'] =df['age'].fillna(0)  # fill the missing value in  age  col with 0

df['age'] =df['age'].fillna(df['age'].mean()).astype(int)
df['salary'] =df['salary'].fillna(df['salary'].mean()).astype(int)
df['name'] =df['name'].fillna("unknown")
print(df)
"""

# task :1 
"""
1. dataframe 
2. head , tail , describe , info , describe(all)
3. count  missing value  
4. fill missing value ===> fill ===> 0 
5. fill missing value  ===>mean 
"""

"""
MCAR : missing completely at random
        ex : 
        name     salary 
        nan      nan
        ved      50000
        nan      nan
        jay      50000

MAR  : missing at random  :
    ex : 
        name     salary 
        sumit    50000
        ved      50000
        nan      7000 
        jay      5000
        
MNAR : missing not at random 
    ex : 
    gender    salary 
    male      50000
    female    50000
    nan       7000
    nan       5000
    nan       6000

""" 

# loc , iloc  : 

