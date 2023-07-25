import numpy as np
from sklearn import datasets, svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()
#split in features and labels
X = iris.data
y = iris.target

classes = ['Iris Setosa', 'Iris Versicolour', 'Iris Virginica']

print(X.shape)
print(y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

'''
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
'''

model = svm.SVC()
model.fit(X_train, y_train)
print(model)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print('Predction:', predictions)
print('Actual:', y_test)
print('Accuracy:', accuracy)

for i in range(len(predictions)):
    print(classes[predictions[i]])
    

    
    