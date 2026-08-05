# merges two dataframes : 

import pandas as pd
df1 = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'David']
})

df2 = pd.DataFrame({
    'id': [3, 4, 5, 6],
    'age': [24, 30, 18, 40]
})

# join  : 
"""
inner   :possible when atleat one  column is common.
outer   :unmatch  col 
left    :left table print  all cols and  right  tables only matches rows 
right   :right table print  all cols and  left  tables only matches rows
fulljoin: all rows from both tables
"""
# inner :
"""
join = pd.merge(
    df1,
    df2,
    how='inner',
    on='id'
)
print("Df1 : \n",df1)
print("Df2 : \n",df2)
print("inner join is  : \n",join)
"""

# right join  :
"""
join = pd.merge(
    df1,
    df2,
    how='right',
    on='id'
)
print("Df1 : \n",df1)
print("Df2 : \n",df2)
print("right join is  : \n",join)
"""
"""
right join is  :             
    id     name  age      
0   3  Charlie   24
1   4    David   30
2   5      NaN   18
3   6      NaN   40

left join is  : 
    id     name   age
0   1    Alice   NaN
1   2      Bob   NaN
2   3  Charlie  24.0
3   4    David  30.0
"""
# left join :
"""
join = pd.merge(
    df1,
    df2,
    how='left',
    on='id'
)
print("Df1 : \n",df1)
print("Df2 : \n",df2)
print("left join is  : \n",join)
"""

# outer join :

"""join = pd.merge(
    df1,
    df2,
    how='outer',
    on='id'
)
print("Df1 : \n",df1)
print("Df2 : \n",df2)
print("outer join is  : \n",join)
"""

# full join :

"""join = pd.merge(
    df1,
    df2,
    how='full',
    on='id'
)
print("Df1 : \n",df1)
print("Df2 : \n",df2)
print("full join is  : \n",join)  # not possible  bcz of  matching  rows 
"""

# task : 
"""
1. remove the  unnamed col  with two dataset : movies and directors 
2. perform the inner join  between the two datasets : with director_id 
"""

