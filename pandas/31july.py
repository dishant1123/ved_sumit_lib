import pandas as pd 

"""
df =pd.DataFrame({
    "id" :[101,102,103,104,105,106,107,108], 
    "product":["monitor","keyboard","mouse","monitor","keyboard","mouse","CPU","keyboard"],
    "price":[50000,1200,800,30000,1000,500,15000,150000],
    "quantity":[10,5,2,8,1,3,4,6]
})

print(df)
df = df.drop_duplicates(subset=["product"])
print(df)
"""
# data set  : mckinsey 

df =pd.read_csv("pandas/mckinsey.csv")
# print(df)

# single col print : 
"""
df = df['country']
print(df)
"""
# multiple  col  print : 

"""country_with_population = df[['country','population','life_exp']]
print(country_with_population)
"""
# loc :  label  based  indexing
"""
print(df.loc[0])
print(df.loc[5])
print(df.loc[2:5])  # 2 index start  end 5 index both  points are included 

print(df.loc[5,['country','population','life_exp']])
print(df.loc[5,'country':'life_exp'])
"""

# iloc :  integer  based  indexing

"""
print(df.iloc[5])
print(df.iloc[2:5])  # 2 index start  end 5 index end  point is excluded 
print(df.iloc[0:3])

print(df.iloc[1:5,0:2])
print(df.iloc[1:10:2 ,1:5:2 ])
"""

# task :1 print country = Aus , life_exp ,population 

# task :2 print only those rows  country =Belgium  and  life_exp >70 

"""belguim =df[(df['country']=="Belgium") & (df['life_exp']>70)]
print(belguim)
"""

# outlier :

df =pd.DataFrame({
    "id" :[101,102,103,104,105,106,107,108], 
    "product":["monitor","keyboard","mouse","monitor","keyboard","mouse","CPU","keyboard"],
    "price":[50000,1200,800,30000,1000,500,15000,150000],
    "quantity":[10,5,2,8,1,3,4,6]
})

print(df)

# 2 method  : 
"""
1.IQR  : interquartile range

    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
2.z-score :
"""
"""
Q1 = df['price'].quantile(0.25)
Q3 = df['price'].quantile(0.75)

print("Q1 = ",Q1)  # 950 
print("Q3 = ",Q3)  # 35000 

IQR = Q3 - Q1
print("IQR = ",IQR)  

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR 

print("lower_bound = ",lower_bound)  
print("upper_bound = ",upper_bound)

outlier = df[(df['price'] < lower_bound) | (df['price'] > upper_bound)]
print(outlier)
"""
# z-score :

from scipy import stats

df['z_score'] = stats.zscore(df['price'])
print(df)

outlier = df[df['z_score'] > 2]
print(outlier)

# next session  :sort,join , winsorization ,captilization 