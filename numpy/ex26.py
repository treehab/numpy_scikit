'''
Rayleigh Distribution - signal processing
scale - standard deviation, how flat the distribution is, default 1.0
size - shape of the returned array
'''

from numpy import random
import numpy as np

x = random.rayleigh(scale=2, size=(2,3))
print(x)

import matplotlib.pyplot as plt
import seaborn as sns

sns.kdeplot(random.rayleigh(size=1000))
plt.show()
