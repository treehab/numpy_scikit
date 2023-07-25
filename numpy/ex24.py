'''
Exponential Distribution - describe time till next event
eg, failure / success
scale - inverse of rate (like lam), default 1.0
size - shape of returned array
'''

from numpy import random
import numpy as np

x = random.exponential(scale=2, size=(2,3))
print(x)

import matplotlib.pyplot as plt
import seaborn as sns

sns.kdeplot(random.exponential(size=1000))
plt.show()

'''
Poisson vs Exponential
num of occurences of an event in a time period vs time between these events
'''