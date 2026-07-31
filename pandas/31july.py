import pandas as pd 

"""df =pd.DataFrame({
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