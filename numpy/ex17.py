'''
Seaborn module
    library using Matplotlib to plot graphs
    visualize random distributions
Distplots - distribution plots of points in an array
'''

import matplotlib.pyplot as plt
import seaborn as sns

sns.kdeplot([0,1,2,3,4,5])
plt.show()

sns.displot([0,1,2,3,4,5])
plt.show()

sns.histplot([0, 1, 2, 3, 4, 5])
plt.show()


