# dataframe : 
"""
2 ways :
1. dict 
2. list 
"""
import pandas as pd 
import numpy as np 
# ex :1 creating  dataframe using  dict 

"""df =pd.DataFrame({
    'id' :[101,102,103,104,105],
    'name' :['saloni','ved','sumit','jay','aakash'],
    'age' :[23,29,27,31,30],
    'salary' :[45000,50000,60000,np.nan,78000]
})
print(df)
print(df.shape)
print(df.columns)

df = df.rename(columns={'name':'student_name','age':'student_age','salary':'student_salary'})  # rename  col 
df['city']=['mumbai','delhi','kolkata','chennai','hyderabad']  # add new col
print(df)
print(df.head(2))
print(df.tail(2))
print(df.info())
print(df.describe())
print(df.describe(include='all'))
"""

# ex :2 creating dataframe using list

"""df =pd.DataFrame([
    [101,'saloni',23,45000,'mumbai'],
    [102,'ved',29,50000,'delhi'],
    [103,'sumit',27,60000,'kolkata'],
    [104,'jay',31,np.nan,'chennai'],
    [105,'aakash',30,78000,'hyderabad']
],columns=['id','name','age','salary','city'])

print(df)
"""

# ex :URL  :
"""df =pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
print(df.head())

"""
# ex : JSON  file  
"""df =pd.read_json("https://jsonplaceholder.typicode.com/users")
print(df.head())
"""

# ex : SQL  file

import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="employees",
    port=3306
)

df = pd.read_sql("SELECT * FROM emp", conn)
print(df)

conn.close()

# 