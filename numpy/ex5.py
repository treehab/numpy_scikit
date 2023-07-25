#copy vs view 
# new array vs view of original array

import numpy as np

#COPY
arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

#VIEW
y = arr.view()
arr[0] = 34

print(arr)
print(y)

#MAKE CHANGES TO VIEW
z = arr.view()
z[0] = 26

print(arr)
print(z)


'''
copies own data
views don't own data
attribute = base
returns None if array owns data,
otherwise attribute refers to the original object
'''

print(x.base)
print(y.base)

