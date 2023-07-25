import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

housing = datasets.fetch_california_housing()


#features and labels
X = housing.data
y = housing.target

print('X')
print(X)
print(X.shape)
print('y')
print(y)
print(y.shape)

#algorithm
lin_reg = linear_model.LinearRegression()

'''
CHECK FOR BEST VALUE OF i

for i in range(8):
    plt.scatter(X.T[i],y)
    plt.show()
'''
plt.scatter(X.T[0], y)
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#train
model = lin_reg.fit(X_train, y_train)
predictions = model.predict(X_test)
print('Predictions:', predictions)
print('R*2 value:', lin_reg.score(X, y))
print('Coefficient:', lin_reg.coef_)
print('Interecpt', lin_reg.intercept_)

