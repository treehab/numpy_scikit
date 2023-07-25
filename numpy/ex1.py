import numpy as np
print(np.__version__)

arr = np.array([1, 2, 3, 4, 5])
print(arr)

#creates array object ndarray
print(type(arr))

#dimensions in array - array depth
#0-D arrays -> elements in array
arr = np.array(42)

print(arr)

#1-D arrays -> has 0-D elements in array
arr = np.array([1, 2, 3, 4, 5])

print(arr)

#2-D arrays -> contains 2 arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)

#3-D arrays -> contains 2 2-D arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)

#dimensions of array
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#higher dimensions
#5th dim has 4 elements
#4th dim has 1 element with vector
#3rd dim has 2D array (1 element as matrix with vector)
#2th dim has 3D array
#1st dim has 4D array
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)
