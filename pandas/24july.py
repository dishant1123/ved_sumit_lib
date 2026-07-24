# pandas : python  library , use data cleaing 
"""
1.data  cleaning  
2.data analysis  :  tops 3 product 
3.join ,merge
4. read any dataset : xlsx ,csv,tsv,json.sql   

"""
# pip install pandas 

import pandas as pd 
import numpy as np

# seris : 
"""a =pd.Series([12,23,35,46,58,69,71,38,69,110])
print(a)

b= pd.Series([90,89,78,56,99],['ram','sita','sumit','ved','prakash'])
print(b)

c= pd.Series([90,89,78,56,99],index=['ram','sita','sumit','ved','prakash'])
print(c)

d=pd.Series({'ram':90,'sita':89,'sumit':78,'ved':56,'prakash':99})
print(d)

e=pd.Series([34,56,78,90],dtype=float)
print(e)

f=pd.Series(["ram",34,56,78,90,34.90,True])
print(f)
print(f.dtypes)
""" 

# head() , tail() , describe() , info() , describe(all)

"""a=pd.Series({"ravan":88,'ram':np.nan,'sita':89,'sumit':78,'ved':56,'prakash':99})
a['ravan'] =66
a['laxman']=55
print(a)

print(a.head())   # first 5 rows  if arg is  not  give 
print(a.head(3))

print(a.tail())  # last 5 rows if  arg is  not give 
print(a.tail(3))

print(a.dtypes)  # data type
print(a.info())
print(a.describe())
print(a.describe(include='all')) #
print(a.keys())
print(a.values)
print(a.items)
"""

# read csv file   : 

"""df =pd.read_csv("pandas/students.csv")
print(df)
print(df.head(2))
print(df.tail(2))
print(df.info())
print(df.describe())
print(df.describe(include='all'))
"""

# tsv file : tab separated value 

"""df =pd.read_csv("pandas/students_age.tsv",sep='\t')
print(df)
"""

# json file :

"""df=pd.read_json("pandas/students.json")
print(df)
"""
