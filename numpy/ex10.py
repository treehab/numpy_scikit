'''
splitting arrays
    reverse of joining(concatenate/stack)
    array_split()
'''


#1D array
#splits 1 array into 3 arrays
import numpy as np

arr = np.array([1,2,3,4,5,6])

new_arr = np.array_split(arr,3)
print(new_arr)

new_arr = np.array_split(arr, 3)
print(new_arr[0])
print(new_arr[1])
print(new_arr[2])


#2D array
#returns 3 2D arrays
arr = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
new_arr = np.array_split(arr,3)
print(new_arr)


arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
new_arr = np.array_split(arr,3, axis=1)
print(new_arr)


'''
split 2D array into 3 2D arrays along rows
    hsplit()
similarly
    vsplit()
    dsplit()
'''
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
new_arr = np.hsplit(arr,3)
print(new_arr)

