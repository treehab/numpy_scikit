'''
Chisquare Distribution - basis to verify hypothesis
df - degree of freedom
size - shape of the returned array
'''

from numpy import random
import numpy as np

x = random.chisquare(df=2, size=(2,3))
print(x)

import matplotlib.pyplot as plt
import seaborn as sns

sns.kdeplot(random.chisquare(df=1, size=1000))
plt.show()
