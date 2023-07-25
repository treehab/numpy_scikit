'''
Random Permutations of Elements
    arrangements of elements
    shuffle()
    permutation()
'''

from numpy import random
import numpy as np

#shuffling arrays
#   makes changes to the original array
arr = np.array([1,2,3,4,5])
random.shuffle(arr)
print(arr)


#generating permutations
#   leaves original array unchanged
arr = np.array([1,2,3,4,5])
print(random.permutation(arr))
