# pip install matplotlib 

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
matplotlib : 

1. plt.plot ===> line plot 
2. plt.scatter ===> scatter plot 
3. plt.bar ===> bar plot 
4. plt.hist ===> histogram 
5. plt.boxplot ===> box plot 
6. plt.pie ===> pie chart 
7. plt.imshow ===> image plot
8. plt.title ===> title
9. plt.xlabel ===> x-axis label
10. plt.ylabel ===> y-axis label
11. plt.legend ===> legend
12. plt.show ===> show plot
13. plt.savefig ===> save plot
14. plt.grid ===> grid
15. plt.legend ===> legend
"""


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
    "Salary":[35000,42000,38000,45000,41000,39000,36000,37000,200000,40000],
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

# line  plot : 
plt.plot(df['Salary'],
         color='red',
         linewidth=2)

plt.title("Experience vs Salary")
plt.xlabel("Salary")
plt.show()