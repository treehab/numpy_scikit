#array slicing
#[start:end]
#[start:end:step]
# start considered 0
# step considered 1

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])
#4th to end element
print(arr[4:])
#beginning to 4th element (not included)
print(arr[:4])

#negative slicing
print(arr[-3:-1])
#excluding last one

#step of slicing
print(arr[1:5:2])
#excluding last one

#every 2nd element from start to end
print(arr[::2])

#slicing 2D arrays
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])
#print 1 to 4 of 2nd array

#return element 2 from both arrays
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 2])
print(arr[0:2, 1:4])
