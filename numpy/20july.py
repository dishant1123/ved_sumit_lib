# slicing , loadtxt, genfromtxt :
import numpy as np

"""arr =np.array([1,4,5,7,89,90,23,11,22])

print(arr)
print(arr[2:5])  # start index 2 end ending 5 
print(arr[2: ])
print(arr[:5])
print(arr[:])
print(arr[1:6:2])# start 1 ending 6 step  2 
print(arr[ : : 2])
print(arr[ : : 3])
print(arr[-1])
print(arr[-5 :-2])
print(arr[-2 :-5 :-1])
print(arr[ : :-1])
"""

# 2d array slicing : 

arr=np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
])

# print(arr)
print(arr[3])
print(arr[1:3])
print(arr[1:4:2])
print(arr[1:3,1:3])# row slicing  1:3 col slicing 1:3
print(arr[:,2:4])
print(arr[0:4:2,1:2])
print(arr[1:3:2, : : -1])

# arr[1:3:2,1:3] =99  # facncy indexing 
# print(arr)

# print : [[2,8,14,20]]

print(arr[[0,1,2,3],[1,2,3,4]])


"""
task :1 take a 2d array 5*5 all element are 1 . and  print  like  this  .
hint  : use  np.ones () , slicing  ,  fancy indexing
input  : 
1 1 1 1 1 
1 1 1 1 1 
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1

output :
1 1 1 1 1 
1 0 0 0 1 
1 0 9 0 1
1 0 0 0 1
1 1 1 1 1.

task :2 take a 2d array 5*5  . and  print  like  this  .

input  : 
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25

output  : [[4,5],
            [19,20],
            [24,25]]

task :3 take a 2d array 5*5  . and  print  like  this  .

input  : 
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25

output   : [[8,9],
            [17,18]]



"""
