import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
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
    "Salary":[52000,42000,38000,67000,41000,40000,77000,89000,200000,40000],
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
# print(df)

# bar plot :

"""bar =plt.bar(df['Name'],df['Salary'],color='red',align='center',alpha=0.5,width=0.5)
plt.title("Salary vs Name")
plt.xlabel("Name")
plt.ylabel("Salary")

for i in bar :
    plt.text(
        i.get_x() + i.get_width()/2,
        i.get_height()+1,
        i.get_height(),
        ha='center',
        fontsize=8,
        color='black'
        
    )
plt.legend(labels=["Salary"],loc='upper right')
plt.grid(True)
plt.show()
"""

# line plot :

"""days =[1,2,3,4,5,6,7,8,9,10]
sales =[2000,3000,1500,1000,900,2400,3000,5600,4800,5100]

line =plt.plot(days,sales,color='red',linewidth=2)
plt.title("Sales vs Days")
plt.xlabel("Days")
plt.ylabel("Sales")

for i in range (len(days)) :
    plt.text(
        days[i],
        sales[i],
        str(sales[i]),
        ha='center',
        fontsize=8,
        color='black'
        
    )
    
plt.grid(True)
plt.legend(labels=["Sales"],loc='upper right')
plt.show()
"""

# scatter plot :

"""plt.scatter(df['Salary'],df['Experience'],color='red',alpha=0.5,s=100)
plt.title("Salary vs Experience")
plt.xlabel("Salary")
plt.ylabel("Experience")
plt.show()
"""

# box plot :

"""plt.boxplot(df['Salary'])
plt.title("Salary")
plt.show()
"""

# subplot :
"""plt.figure(figsize=(10,10))

plt.subplot(2,2,1)
plt.plot(df['Salary'],color='red',linewidth=2)
plt.title("Salary vs Name")
plt.xlabel("Name")
plt.ylabel("Salary")


plt.subplot(2,2,2)
plt.barh(df['Department'],df['Salary'],color='red',align='center',alpha=0.5)
plt.xlabel("Department")
plt.ylabel("Salary")

plt.subplot(2,2,3)
plt.boxplot(df['Salary'])

plt.subplot(2,2,4)
plt.scatter(df['Salary'],df['Experience'],color='red',alpha=0.5,s=100)
plt.xlabel("Salary")
plt.ylabel("Experience")

plt.show()
"""

# pie chart :

plt.pie(df['Salary'],labels=df['Name'],autopct='%1.1f%%')
plt.title("Salary")
plt.show()