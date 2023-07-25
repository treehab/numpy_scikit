#shape of array
#shows the dimensions
import numpy as np
arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr.shape)


'''
specifying 5 dimensions
[[[[[1 2 3 4]]]]]
'''
arr = np.array([1,2,3,4], ndmin=5)
print(arr)
print('shape of array:', arr.shape)
