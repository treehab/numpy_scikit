'''
Data Distribution - list ofpossible values and how often they occur
'''

'''
Random Distribution
Probablility Density Function - describes continous probability
p shows probablity of occurence of each in array
sum of p = 1
'''
from numpy import random
x = random.choice([5,7,4,3], p=[0.1,0.0,0.7,0.2], size=(10))
print(x)

#2D
x = random.choice([1,5,3,2], p=[0.3,0.3,0.2,0.2], size=(3,5))
print(x)


