#array indexing
# accessing an array element

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])

print(arr[2] + arr[3])

#access 2D arrays
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print('2nd element on 1st row: ', arr[0, 1])

#access 3D arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])
#0 - 1st dim = 2D array [[1,2,3], [4,5,6]]
#1 - 2nd dim = 2D array [4,5,6]
#2 - 3rd dim = 2nd element = 6

#negative indexing
#prints last element
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print('Last element from 2nd dim: ', arr[1, -1])

