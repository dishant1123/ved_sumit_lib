"""
1. line  plot  : using  group  by  order date 
2. scatter  plot : sales ,profit 
3. bar chart  : category vs sales 
4. figure axis 
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# line  plot : 

"""
df=pd.read_csv("matplotlib/sample_superstore (1).csv")

lines = df.groupby(['Order Date'])['Sales'].sum()

plt.plot(lines.index,lines.values,linewidth=2,linestyle='-',color='red')
plt.title("Sales vs Order Date")
plt.xlabel("Order Date")
plt.ylabel("Sales")
plt.xticks(rotation=60)
plt.grid(True)
plt.legend(labels=["Sales"],loc='upper right')
plt.show()
"""

# scatter plot :

"""
df=pd.read_csv("matplotlib/sample_superstore (1).csv")

plt.scatter(df['Sales'],df['Profit'],color='red',alpha=0.5,s=100)
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.grid(True)
plt.show()
"""

# bar chart :

df=pd.read_csv("matplotlib/sample_superstore (1).csv")

category_sales = df.groupby(['Category'])['Sales'].sum()
plt.bar(category_sales.index,category_sales.values,color='red',align='center',alpha=0.5,width=0.5)

for i , j in enumerate(category_sales.values) :
    plt.text(
        i,
        j,
        f"{j:.2f}",
        ha='center',
        fontsize=8,
        color='black'
    )

plt.title("Sales vs Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.grid(True)
plt.show()


# figure axis :

"""df=pd.read_csv("matplotlib/sample_superstore (1).csv")

fig,ax = plt.subplots(2,2,figsize=(15,10))
category_sales = df.groupby(['Category'])['Sales'].sum()
region_sales = df.groupby(['Region'])['Sales'].sum()

ax[0,0].plot(df['Sales'],df['Profit'],linewidth=2,linestyle='-',color='red')
ax[0,0].set_xlabel("Sales")
ax[0,0].set_ylabel("Profit")

ax[0,1].bar(category_sales.index,category_sales.values,color='red',align='center',alpha=0.5,width=0.5)
ax[0,1].set_xlabel("Category")
ax[0,1].set_ylabel("Sales")

ax[1,0].scatter(df['Sales'],df['Discount'],color='red',alpha=0.5,s=100)
ax[1,0].set_xlabel("Sales")
ax[1,0].set_ylabel("Discount")

ax[1,1].barh(region_sales.index,region_sales.values,color='red',align='center',alpha=0.5)
ax[1,1].set_xlabel("Region")
ax[1,1].set_ylabel("Sales")

plt.show()
"""