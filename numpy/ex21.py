'''
Uniform Distribution - every event has equal chances of occuring
eg, generation of random numbers
a - lower bound ,default 0.0
b - upper bound ,default 1.0
size - shape of the returned array
'''

from numpy import random
import numpy as np

x = random.uniform(size=(2,3))
print(x)

import matplotlib.pyplot as plt
import seaborn as sns

sns.kdeplot(random.uniform(size=1000))
plt.show()
