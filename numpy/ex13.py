'''
Filtering arrays

value = True --> included in filtered array
value = False --> excluded from filtered array
'''

import numpy as np
arr = np.array([41,42,43,44])
x = [True, False, True, False]

new_arr = arr[x]
print(new_arr)


#creating the filter array
filter_arr = []
for element in arr:
    if element>42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
        
new_arr = arr[filter_arr]
print(filter_arr)
print(new_arr)


#filter array returning only even numbers
arr = np.array([1,2,3,4,5,6,7])

filter_arr = []
for element in arr:
    if element % 2 == 0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
        
new_arr = arr[filter_arr]
print(filter_arr)
print(new_arr)


#creating filter directly from array
#only return values > 41
arr = np.array([39,40,41,42,43,44,45])

filter_arr = arr > 41
new_arr = arr[filter_arr]

print(filter_arr)
print(new_arr)

#return only even elements
filter_arr = arr % 2 == 0
new_arr = arr[filter_arr]

print(filter_arr)
print(new_arr)
