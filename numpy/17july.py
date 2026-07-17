"""
1. maths : + - * / 
2. stats function  : mean , std , var , sum , max , min , argmax , argmin ,
3. linear algebra  : inv , det ,T 
4. loadtxt , genfromtxt 
5.random  module  
6.matrix multiplication
7. flattern ,ravel 
"""

import numpy as np

# maths function  : + - *  / % 
"""
arr=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
arr1=np.array([
    [6,7,8],
    [9,10,11],
    [12,13,14]
])
    
print(arr)
print(arr1)
print("addition :-\n",arr+arr1)
print("subtraction :-\n",arr-arr1)
print("multiplication :-\n",arr*arr1)  # it is not  matrix multiplication
print("division :-\n",arr/arr1)
print("remainder :-\n",arr%arr1)
"""
# matrix  multiplication : np.matmul,np.dot ,a@b 
"""
arr=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
arr1=np.array([
    [6,7,8],
    [9,10,11]
    [12,13,14]
])

matrix_maultiplication=np.matmul(arr,arr1)
matrix_maultiplication=np.dot(arr,arr1)
print("matrix multiplication :-\n",matrix_maultiplication)
print("matrix multiplication :-\n",arr@arr1)
"""

# ex : 

"""a = np.array([
    [1],
    [2],
    [3]
])
b=np.array([
    [6,7,8],
    [9,10,11],
    [12,13,14]
])

print(a)
print(a.shape)
print(a@b) # not  possible  
print(a*b)
"""

# indetity matrix , transpose matrix

"""
a=np.array([
    [6,7,8],
    [9,10,11],
    [12,13,14]
])

# print(np.identity(3))
print(a)
print(a.T)  # transpose matrix
print(np.transpose(a))
"""

# stats function  : mean , std , var , sum , max , min , argmax , argmin 

"""
a=np.array([
    [6,7,8],
    [9,4,11],
    [12,13,14]
])   # 4 6 7 8 9 11 12 13 14 
print(a.mean())
print(np.median(a))
print(a.std())
print(a.var())

print(a.sum())
print(a.sum(axis=0))  # sum  of col wise 
print(a.sum(axis=1))  # sum  of row wise

print(a.max())
print(a.max(axis=0))  # max  of col wise
print(a.max(axis=1))  # max  of row wise

print(a.argmax())
print(a.argmax(axis=0))  # argmax  of col wise  ===> max value index 
print(a.argmax(axis=1))  # argmax  of row wise

print(a.min())
print(a.min(axis=0))  # min  of col wise
print(a.min(axis=1))  # min  of row wise

print(a.argmin())
print(a.argmin(axis=0))  # argmin  of col wise  ===> min value index 
print(a.argmin(axis=1))  # argmin  of row wise
"""

# linv al : 

"""
a=np.array([
    [6,7,8],
    [9,4,11],
    [12,13,14]
])   # 4 6 7 8 9 11 12 13 14 

result =np.linalg.det(a)
result =np.linalg.inv(a)
print(result)
"""

# random  module  : 

import random 

"""# arr = np.random.random((3,3))  #  between 0 and 1
# arr =np.random.randint(low=1, high=140,size=(4,3))
arr =np.random.sample(6)
print(arr)
"""

# shallow copy  :
"""l1 =[1,2,34,56,78]

l2=l1
l2[3] =99 
print("l1 = \n",l1)
print("l2 = \n",l2)
"""
# deep copy  : 
"""l1 =[1,2,34,56,78]

l2=l1.copy()
l2[3] =99 
print("l1 = \n",l1)
print("l2 = \n",l2)
"""
# flatten  :  convert any demensional array to 1d array. 

"""a=np.array([
    [6,7,8],
    [9,4,11],
    [12,13,14]
])   
f_array=a.flatten()

f_array[2]=99

print("original array :-\n",a)
print("flattern array :-\n",f_array)
"""
# ravel :  convert any demensional array to 1d array. 
a=np.array([
    [6,7,8],
    [9,4,11],
    [12,13,14]
])   
r_array=a.ravel()

r_array[2]=99

print("original array :-\n",a)
print("ravel array :-\n",r_array)

