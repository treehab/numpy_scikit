'''
Normal (Gaussian) Distribution - continuous distribution
    IQ Scores, Heartbeats, etc
    random.normal()
    loc - Mean:peak of bell
    scale - Standard Deviation: how flat the graph distribution should be
    size - shape of returned array
'''

#random normal distribution of size 2*3
from numpy import random
x = random.normal(size=(2,3))
print(x)

#same with mean at 1 and standard deviation at 2
x = random.normal(loc=1, scale=2, size=(2,3))
print(x)

#visualization of normal distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.normal(size=1000))
plt.show()

sns.histplot(random.normal(size=1000))
plt.show()

sns.kdeplot(random.normal(size=1000))
plt.show()
