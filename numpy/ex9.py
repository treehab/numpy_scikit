'''
joining arrays
    concatenate() function
'''

#1D array
import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arr = np.concatenate((arr1,arr2))

print(arr)


#2D arrays
arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])

arr = np.concatenate((arr1,arr2))
print(arr)

arr = np.concatenate((arr1, arr2), axis=1)
print(arr)



'''
joining arrays using stack functions
    same as concatenation
    but stack() is done along a new axis
    putting them over one another
'''

#1D array
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr)

#2D arrays
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

arr = np.stack((arr1, arr2), axis=1)
print(arr)


'''
stacking along rows
    hstack()
'''
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))

print(arr)


'''
stacking along columns
    vstack()
'''
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print(arr)


'''
stacking along height/depth
    dstack()
'''
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print(arr)
