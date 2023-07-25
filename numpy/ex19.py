'''
Binomial Distribution - Discrete Distributon eg, coin toss (not like continous distribution - height)
n - num of trials
p - prob of occurence of each trial
size - shape of returned array
'''

from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x = random.binomial(n=4,p=0.7,size=8)
print(x)

sns.kdeplot(random.binomial(n=6, p=0.3, size=100))
plt.show()

sns.histplot(random.binomial(n=6, p=0.3, size=100))
plt.show()


'''
Normal distribution = continuous
Binomial Dsitribution = discrete
'''
sns.kdeplot(random.normal(loc=50, scale=5, size=1000), label='normal')
sns.kdeplot(random.binomial(n=100, p=0.5, size=1000), label='binomial')
plt.show()

