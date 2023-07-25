'''
Poisson Distribution - Discrete Distribution
    estimates how many times an event can happen in a specified time
    eg, If someone eats twice a day what is th eprob he will eat thrice
    lam - rate/known num of occurences
    size - shape of returned array
'''

from numpy import random
x = random.poisson(lam=2,size=10)
print(x)

import matplotlib.pyplot as plt
import seaborn as sns

sns.kdeplot(random.poisson(lam=2, size=1000))
plt.show()


'''
Normal vs Poisson
continuous vs discrete
'''
sns.kdeplot(random.normal(loc=50, scale=7, size=1000), label='normal')
sns.kdeplot(random.poisson(lam=50, size=1000), label='poisson')
plt.show()


'''
Binomial vs Poisson
only two outcomes vs unlimited possible outcomes
for large n and near-zero p --> binomial  is nearly identical to poisson
n*p is nearly equal to lam
'''
sns.kdeplot(random.binomial(n=1000, p=0.01, size=1000),label='binomial')
sns.kdeplot(random.poisson(lam=10, size=1000), label='poisson')
plt.show()
