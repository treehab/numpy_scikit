'''
Pareto Distribution - follows Pareto's Law
    80-20 distribution
    20%_factors cause 80%_outcome
    a - shape parameter
    size - shape of returned array
'''

from numpy import random
import numpy as np

x = random.pareto(a=2, size=(2,3))
print(x)

import matplotlib.pyplot as plt
import seaborn as sns

sns.kdeplot(random.pareto(a=2, size=1000))
plt.show()

