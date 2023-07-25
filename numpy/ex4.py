#data types
#str, int, float, boolean, complex
'''
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
'''
import numpy as np

#checking datatype (.dtype)
arr = np.array([1, 2, 3, 4])

print(arr.dtype)

arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype)

#arrays with defined data type
#string datatype of numbers
arr = np.array([1, 2, 3, 4], dtype ='S')

print(arr)
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)

#converting datatype on existing array (.astype(' '))
arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)
