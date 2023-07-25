'''
Logistic Distribution - describes growth 
used for logistic regression, neural networks, etc
loc - mean, where the peak is, default 0
scale - standard deviation, flatness of distribution, default 1
size - shape of returned array
'''

from numpy import random
import numpy as np

x = random.logistic(loc=1, scale=2, size=(2,3))
print(x)

import matplotlib.pyplot as plt
import seaborn as sns

sns.kdeplot(random.logistic(size=1000))
plt.show()


'''
Logistic vs Normal Distribution
logistic represents more possibility of occurence of any event further away from mean
for high scale(standard deviation) normal and logistic are nearly identical
'''

sns.kdeplot(random.normal(scale=2, size=1000), label='normal')
sns.kdeplot(random.logistic(size=1000), label='logistic')
plt.show()
