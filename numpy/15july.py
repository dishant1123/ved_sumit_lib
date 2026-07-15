# python : 
"""
1. list   : mutable  , []
2. dict   : mutable , {}  ==> key : value
3. tuple  : immutable  ===> ()
4. set    : mutable , only  unique element 
5. string : immutable 
"""
"""
libraries : 
1. numpy 
2. pandas
3. matplotlib
4. seaborn 
"""

# numpy : matrix , 1d,2d ,3d , broardcasting ,data analysis , list to convert array 
"""
numpy store data  hemogeneous . 
# pip install numpy

"""
import numpy as np 

# np.array () :  
"""a =np.array([1,2,3,4,5,6,7,8])
print(a)
print(type(a))
print(a.ndim)  # number of dimension

b=np.array([12,13,90.78,123])
print(b)

c=np.array([
    [1,2,3],
    [4,5,6]
])

# array  attributes : 
print(c)
print(c.shape)
print(c.ndim)
print(c.size)
print(c.itemsize)
print(c.nbytes)

d= np.array([
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [7,8,9],
        [10,11,12]
    ]
    ]
)
print(d)
print(d.shape)
"""

# np.arange(),reshape() : 

"""a=np.arange(10)
print(a)

b=np.arange(10,20)  # start , stop  
print(b)

c=np.arange(1,20,3)  # start , stop  ,step  
print(c)

d=np.arange(1,10,dtype="int")  # start , stop  ,step
print(d)

e=np.arange(1,21).reshape(5,4)
print(e)

f=np.arange(1,21,2).reshape(2,5)
print(f)

result = np.arange(1,33).reshape(2,2,2,4)
print(result)
"""
# np.zeros(),np.ones(),np.full(),np.linespace() :

a=np.zeros(10,dtype="int").reshape(5,2)
print(a)

b=np.ones(10,dtype="int").reshape(5,2)
print(b)

c=np.full(10,fill_value=10,dtype="int").reshape(5,2)
print(c)

result =np.full_like(a,fill_value=100)
print(result)

arr =np.linspace(1,12,3)  # stop -start /step -1   : 12 -1 / 2
print(arr)