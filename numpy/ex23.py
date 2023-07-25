'''
Multinomial Distribution - generalized Binomial Distribution
n - no of possible outcomes eg, 6 for dice
pvals - list of probablity of outcomes eg,[1/6,1/6,1/6,1/6,1/6,1/6] for dice
size - shape of returned array
'''

from numpy import random
import numpy as np

x = random.multinomial(n=6, pvals=[1/6,1/6,1/6,1/6,1/6,1/6])
print(x)

