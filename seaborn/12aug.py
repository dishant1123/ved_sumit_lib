"""
seaborn : statistics and visualizations

----> less code , dataset read 

teheme : 
set_theme(style="darkgrid")
sns.set_theme(style="whitegrid")
sns.set_theme(style="white")
sns.set_theme(style="dark")
sns.set_theme(style="ticks")


1. histogram : distribution of total_bill ,add kde = true
2. KDE : compare the smoker and  non-smoker distribution
3. count plot : count the  customers visit today 
4. box plot :bill amount differ between days
5. vilon plot : bill amount differ between days ,hue = "smoker"


"""
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


df = sns.load_dataset("tips")
print(df.head(29))

# histogram :

"""plt.figure(figsize=(10,5))
sns.histplot(
    data=df,
    x="total_bill",
    bins=10,
    kde=True,
    )
plt.title("Distribution of total_bill")
plt.show()
"""

# kde :kernel density estimation
"""sns.set_theme(style="darkgrid")
sns.kdeplot(
    data=df,
    x="total_bill",
    hue="smoker",
    
)
plt.title("using KDE distribution of total_bill")
plt.show()
"""

# count plot : 

"""sns.set_theme(style="dark")
plt.figure(figsize=(10,5))

sns.countplot(
    data=df,
    x="day",
    hue="smoker"
)
plt.title("count plot of customers visit today")
plt.show()
"""

# box plot  :

"""
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10,5))

sns.boxplot(
    data=df,
    x="day",
    y="total_bill"
)

plt.title("bill amount differ between days")
plt.show()
"""

# violin plot :

"""sns.set_theme(style="ticks")
plt.figure(figsize=(10,5))

sns.violinplot(
    data=df,
    x="time",
    y="total_bill",
    inner="quartile"
)
plt.title("bill amount differ between days")
plt.show()

"""

# heat map   : 

"""df = df.corr(numeric_only=True)

sns.set_theme(style="darkgrid")
sns.heatmap(df,annot=True,cmap="YlGnBu")
plt.title("correlation matrix")
plt.show()
"""

# scatter plot :

"""sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="smoker"
)
plt.title("scatter plot of total_bill vs tip")
plt.show()
"""

# pair plot :

sns.pairplot(
    data=df,
    hue="smoker",
    kind="reg",
    height=6,
    palette="Set2",
    vars=["total_bill","tip"]
)
plt.show()
