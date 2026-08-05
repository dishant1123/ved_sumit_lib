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

movies=pd.read_csv("pandas/movies.csv")
movies =movies.drop(columns=['Unnamed: 0'])

directors=pd.read_csv("pandas/directors.csv")
directors =directors.drop(columns=['Unnamed: 0'])

# print(movies.head())
# print(directors.head())

# join  : 

"""join_with_director_id = pd.merge(
    movies,
    directors,
    how='inner',
    right_on='id',
    left_on='director_id'
    
)

print("join_with_director_id is  : \n",join_with_director_id)
"""
"""
tasks 

1. top 10 directors with highest number of movies
2. top 10 movies with highest budget
3. top 5 movies with highest revenue
4. bottom 5 movies with very low vote_average
"""

