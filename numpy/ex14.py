'''
Random numbers - that cannot be predicted logically
    Pseudo Random - generated through generation algorithm
    True Random
'''

#generate a random integer from 0 to 100
#   random.randint()
from numpy import random
x = random.randint(100)
print(x)

#generate a random array
#   random.randint(num, size=())
#6 element array from numbers between 0 to 100
x = random.randint(100, size=(6))
print(x)

#generate a 2D array with 3 rows each containing 5 random integers from 0 to 100
x = random.randint(100, size=(3,5))
print(x)

# generate random float
#   random.rand()
x = random.rand()
print(x)

#1D array with 5 random floats
x = random.rand(5)
print(x)

#2D array with 3 rows each containing 5 random nums
x = random.rand(3,5)
print(x)


'''
Generate random numbers from an array
    choice()
'''
x = random.choice([3,6,8,4])
print(x)

#2D array using size()
x = random.choice([5,7,4,1], size=(3,5))
print(x)



