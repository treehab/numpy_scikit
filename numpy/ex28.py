'''
Zipf Distribution - zipf's law
nth common tern is 1/n times of the most common term
a - distribution parameter
size - shape of the returned array
'''

from numpy import random
import numpy as np

x = random.zipf(a=2,size=(2,3))
print(x)

import matplotlib.pyplot as plt
import seaborn as sns

sns.kdeplot(random.zipf(a=2, size=1000))
sns.kdeplot(x[x<10])
plt.show()


