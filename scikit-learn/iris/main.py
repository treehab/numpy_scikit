from sklearn import datasets
import numpy as np
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()

#split in features and labels
X = iris.data
y = iris.target

print(X,y)
print(X.shape) # 150,4
print(y.shape) # 150,1

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
#test size = 0.2 means that 20% data is for testing purposes
#dont take test size as too low

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

