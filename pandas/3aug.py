"""
1. outlier detection  
2. boxplot 
3. IQR method  
4. z-score method
5. outlier treatment : winsorization , upper_limit , clip
6. data type conversion
7. data convertion  :
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = {
    "Emp_ID":[101,102,103,104,105,106,107,108,109,110],
    "Name":[
        "dishant shah",
        "rahul patel",
        "riya mehta",
        "amit kumar",
        "neha joshi",
        "jay shah",
        "pooja patel",
        "manish",
        "krishna",
        "vivek"
    ],
    "Age":[24,28,25,45,27,26,29,24,31,30],
    "Salary":[35000,42000,38000,45000,41000,39000,36000,37000,2000000,40000],
    "Experience":[2,4,3,18,5,3,4,2,20,5],
    "Department":[
        "IT",
        "HR",
        "IT",
        "Finance",
        "Sales",
        "IT",
        "HR",
        "Sales",
        "Finance",
        "IT"
    ],
    "Joining_Date":[
        "01-01-2022",
        "15-03-2021",
        "10-05-2022",
        "20-07-2010",
        "18-06-2020",
        "11-08-2021",
        "22-09-2022",
        "14-11-2023",
        "01-02-2005",
        "15-12-2019"
    ],
    "Is_Active":[
        "True",
        "False",
        "True",
        "True",
        "False",
        "True",
        "True",
        "False",
        "True",
        "True"
    ]
}
df = pd.DataFrame(data)
print(df)
# print(df.info())

"""plt.boxplot(df['Salary'])
plt.title("boxplot of Salary")
plt.show()
"""

# outlier detection :
"""
Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("lower_bound = ",lower_bound)
print("upper_bound = ",upper_bound)

outlier=df[(df['Salary']<lower_bound) | (df['Salary']>upper_bound)]
print(outlier)
"""
# z-score method :
"""from scipy import stats

df['z_score'] = stats.zscore(df['Salary'])
outlier = df[df['z_score'] > 2]
print(outlier)
"""

# outlier treatment : winsorization , upper_limit , clip

"""lower_bound = df['Salary'].quantile(0.05)
upper_bound = df['Salary'].quantile(0.95)
print("lower_bound = ",lower_bound)
print("upper_bound = ",upper_bound)
df['winsorized_salary'] = df['Salary'].clip(upper=upper_bound)
print(df)
"""

# data type conversion :
"""
df['Salary'] =df['Salary'].astype(int)
print(df)
"""
# map : 

"""df['IS_Active'] = df['Is_Active'].map({"True":1,"False":0})
df.drop(columns=['Is_Active'],inplace=True)
print(df)
"""

# query  : 

"""salary_above_40K =df.query("Department=='IT' and Salary>35000")[['Name','Department','Salary']]
print(salary_above_40K)
"""

# date : 

"""df['Joining_Date'] =pd.to_datetime(df['Joining_Date'],format="%d-%m-%Y")
df['year'] =df['Joining_Date'].dt.year
df['month'] =df['Joining_Date'].dt.month
df['month_name'] =df['Joining_Date'].dt.month_name()
df['day'] =df['Joining_Date'].dt.day
print(df)
"""

# value_counts :
"""
total_department =df['Department'].value_counts()
print(total_department)
"""

# sort_values : 

"""sort_salary = df.sort_values(by='Salary')
sort_salary = df.sort_values(by='Salary',ascending=False)
print(sort_salary)
"""

# groupby : department wise salary  print  

"""department_wise_salary  = df.groupby('Department')['Salary'].sum()
department_wise_salary = df.groupby('Department')['Salary'].agg(['sum','mean','count'])
print(department_wise_salary)
"""

#hw : top 3 emp name highest salary :

