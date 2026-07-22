# Vstack ,Hstack ,loadtxt,genfromtxt,boardcasting  : 

import numpy as np

"""arr=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

arr1=np.array([
    [11,12,13],
    [41,51,61],
    [17,18,19]
])

print(arr)

result =np.vstack((arr,arr1))
print(result)

result1 =np.hstack((arr,arr1))
print(result1)
"""

# boardcasting :
"""
rules :
1. both arrays shapes  are same. 
2. 1 array  is  must be  1d. 
"""

# ex :1 

"""arr=np.array([1,2,3,4,5])

mul_by_5 = arr*5 
print(arr)
print(mul_by_5)
"""

# ex:2 
"""
a=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ])

b=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
result =a+b 
print(result)
"""

# ex :3 

"""a=np.array([[1],
            [2]])   # 2,1 
b=np.array([[1,2,3],
            [3,4,6]])  #  2,3 

print(a)
print(a+b)

"""

# ex :4 

"""a=np.array([1,2,3,4,5])   #1d  5,  
b=np.array([
    [1],
    [2],
    [3],
    [4],
    [5]
])
print(a.shape)
print(b.shape)
print(a+b)
"""

# ex :5   1 shape ===> (1,5) , 2 shape ====> (5,1) dimention  are same 
"""a=np.array([
    [1,2,3,4,5],
])
b=np.array([
    [1],[2],[3],[4],[5]
])
print(a.shape)
print(b.shape)
print(a+b)
"""
# ex :6 

"""a=np.arange(1,7).reshape(3,2)
b=np.arange(1,7).reshape(2,3)
print(a)
print(b)
print(a+b)  # not  possible
"""

# np.loadtxt : clean data , only for number

"""result = np.loadtxt("numpy/1.txt",delimiter=",",dtype=int,skiprows=1)
print(result)

print(result.mean())
print(np.median(result))
print(result[0,0])
print(result[1,1])
"""

# genfromtxt : 

"""
result =np.genfromtxt("numpy/2.txt",delimiter=",",dtype=None,skip_header=1)
print(result)
"""
# missing value  : 

"""result =np.genfromtxt("numpy/2.txt",delimiter=",",dtype=None,skip_header=1,filling_values=0)
print(result)
"""

# filling value  age 23 and marks 99 :

"""result[2][2]=23
result[1][3]=99

print(result)
"""

# conditional  : 

a=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ])

print(a>5)
print(np.where(a>5))