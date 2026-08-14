import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# reg plot , catplot ,displot ,jointplot :

"""sales =[100,250,150,400,500,600,750,800,900]
days =[1,2,3,4,5,6,7,8,9]

sns.set_theme(style="darkgrid")
df=pd.DataFrame({"sales":sales,"days":days})

sns.regplot(
    data=df,
    x="days",
    y="sales",

    scatter=True,
    line_kws={"color":"red"}
    
)

plt.title("sales vs days")
plt.show()
"""

# catplot :

"""df =sns.load_dataset("tips")

sns.catplot(
    data=df,
    x="time",
    y="total_bill",
    hue="smoker",
    kind="bar",
    ci=None
)
plt.title("catplot of total_bill vs time")
plt.show()
"""

# displot :
"""df = sns.load_dataset("tips")
sns.set_theme(style="whitegrid")

plt.figure(figsize=(10,5))
sns.displot(
    data=df,
    x="total_bill",
    hue="smoker",
    kind="kde"
)

plt.title("displot of total_bill")
plt.show()
"""

# jointplot :

"""df=sns.load_dataset("tips")

sns.set_theme(style="darkgrid")
plt.figure(figsize=(10,5))

sns.jointplot(
    data=df,
    x="total_bill",
    y="tip",
    kind='reg', 
    ci=None  
    
)
plt.title("jointplot of total_bill vs tip")
plt.show()
"""

# EDA : Exploratory Data Analysis
"""
step :1 data read 
step :2 data cleaning ----> info,missing value , outlier , 
step :3 inslights 
       1. total  sales
       2. total profit 
       3. region wise sales , category wise sales , sub-category wise sales
       4. region wise profit , category wise profit , sub-category wise profit

step :4 matplotlib plot

"""



