'''
array search
    where()
'''

#shows indexes where value 4 is present
import numpy as np

arr = np.array([1,2,3,4,5,4,4])

x = np.where(arr == 4)
print(x)

#find indexes where values are even
arr = np.array([1,2,3,4,5,6,7,8])

x = np.where(arr%2 == 0)
print(x)

#indexes wher evalues are odd
y = np.where(arr%2 == 1)
print(y)


'''
search sorted
performs binary search in an array 
and returns the index where specific value would 
be inserted to maintain search order
    searchsorted()
'''

#where should number 7 be inserted to remain sort order
arr = np.array([6,7,8,9])
p = np.searchsorted(arr,6)
q = np.searchsorted(arr,7)
r = np.searchsorted(arr,8)
s = np.searchsorted(arr,9)
print(p)
print(q)
print(r)
print(s)

#search from right side
# side = 'right'
a = np.searchsorted(arr, 6,side='right')
b = np.searchsorted(arr, 7, side='right')
c = np.searchsorted(arr, 8, side='right')
d = np.searchsorted(arr, 9, side='right')
print(a)
print(b)
print(c)
print(d)


#multiple values
arr = np.array([1,3,5,7])
x = np.searchsorted(arr, [2,4,6])
print(x)

