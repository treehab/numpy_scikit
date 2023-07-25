#array reshaping

'''
1D to 2D
1 array with 4 arrays each with 3 elements
'''
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

new_arr = arr.reshape(4,3)
print(new_arr)


'''
1D to 3D
2 arrays each with 3 arrays and 2 elements
'''
new_arr = arr.reshape(2,3,2)
print(new_arr)


'''
returns copy or view
'''
arr = np.array([1,2,3,4,5,6,7,8])
print(arr.reshape(2,4).base)
#view since it returns original array


'''
passing unknown -1 dimension
cannot pass in more than one dimension
'''
new_arr = arr.reshape(2,2,-1)
print(new_arr)


'''
flattening arrays
    converting a multidimensional array into a 1D array
'''
arr = np.array([[1,2,3],[4,5,6]])
new_arr = arr.reshape(-1)
print(new_arr)
