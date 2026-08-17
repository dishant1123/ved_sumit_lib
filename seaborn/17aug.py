"""
EDA : exploratory data analysis

step : 1 


"""

import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Sample - Superstore.csv",encoding="ISO-8859-1")
print(df.head(10))

# info ,describe  -----> understand the  data  

"""print(df.info())
print(df.describe())
"""

# missing value, outlier  -----> 
"""
print(df.isnull().sum())
"""
# outlier for sales : 
"""q1= df['Sales'].quantile(0.25)
q3 = df['Sales'].quantile(0.75)

IQR = q3 -q1 
print("IQR :",IQR)

lower_limit = q1 - 1.5 * IQR
upper_limit = q3 + 1.5 * IQR

print("lower limit :",lower_limit)
print("upper limit :",upper_limit)

outlier = df[(df['Sales'] < lower_limit) | (df['Sales'] > upper_limit)]
print(outlier)
"""
# box plot for outlier  fo sales :
"""
plt.boxplot(df['Sales'])
plt.show()"""

# slights : 

# 1. top 5 sub-category  wise profit  bar chart :
"""top_5 = df.groupby(['Sub-Category'])['Profit'].sum().sort_values(ascending=False).head(5)
print(top_5)

# top 5 sub-category  wise profit  bar chart :

plt.bar(top_5.index,top_5)
plt.title("Top 5 Sub-Category wise Profit")
plt.xlabel("Sub-Category")
plt.ylabel("Profit")
plt.show()
"""
# 2. top 5 sub-category  wise sales  bar chart :

"""top_5 = df.groupby(['Sub-Category'])['Sales'].sum().sort_values(ascending=False).head(5)
print(top_5)
"""
# top 5 sub-category  wise profit  bar chart :

"""plt.bar(top_5.index,top_5)
plt.title("Top 5 Sub-Category wise Profit")
plt.xlabel("Sub-Category")
plt.ylabel("Profit")
plt.show()
"""
# 3. sales profit  line 

# 4. category profit, region ,   ----> sales cat , region 

# 5. month year day  wise  sales , profit    ----> to_datetime ----> order_date  

# 6. discount ,sales  ----> graph  ----> relaition  -----> heatmap 

# 7. customer wise profit  , sales  

# 8. product wise profit  , sales

import ydata_profiling as ydp

"""report = ydp.ProfileReport(df, title="Superstore Analysis Report")
report.to_file("Superstore_analysis_report.html")
"""
import sweetviz as sv

report = sv.analyze(df)
report.show_html("sweet_report.html")
