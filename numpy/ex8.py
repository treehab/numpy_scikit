'''
array iterating
    go through elements one by one
'''


#1D array
import numpy as np
arr = np.array([1,2,3])

for i in arr:
    print(i)

    
#2D arrays
arr = np.array([[1,2,3],[4,5,6]])
for j in arr:
    print(j)
#prints 2 arrays with 2 elements

#An n-D array goes through n-1th D one by one
#iterating each scalar element in a 2D array
arr = np.array([[1,2,3],[4,5,6]])

for i in arr:
    for j in i:
        print(j)
#prints numbers 1 to 6


#3D arrays
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

for x in arr:
    print(x)
#prints 2 arrays each with 2 array with 3 elements each

#iterating each element in a 3D array
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

for x in arr:
    for y in x:
        for z in y:
            print(z)
            

'''
iterating arrays using nditer()
'''
#iterating each scalar element 
arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

for i in np.nditer(arr):
    print(i)


'''
iterating arrays with different data types
    op_dtypes using nditer() and extra space flags=['buffered']
'''
arr = np.array([1,2,3])

for i in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(i)
    

'''
iterating with different step size
    iterating through every scalar element with step size of 2
        skipping 1 element/every alternate element
'''
arr = np.array([[1,2,3,4],[5,6,7,8]])

for i in np.nditer(arr[:, ::2]):
    print(i)
    

'''
enumerated iteration using ndenumerate()
    sequence numbers of somethings one by one
        used when we require the corresponding index number while iterating
'''
#1D array
arr = np.array([1,2,3])

for i, j in np.ndenumerate(arr):
    print(i,j)
    
#2D array
arr = np.array([[1,2,3,4],[5,6,7,8]])

for i,j in np.ndenumerate(arr):
    print(i,j)
    

    


