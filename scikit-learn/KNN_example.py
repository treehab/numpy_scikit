import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import neighbors, metrics
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score 

dataset = pd.read_csv('car+evaluation\car.data')
print(dataset. head())

X = dataset[[
    'buying', 
    'maint',
    'safety'
]].values
y = dataset[['class']].values

print(X,y)

#converting X
#converting strings (vhigh,low etc) to numbers
le = LabelEncoder()
#X[0] = 3 --> rows * columns = 1 * 3
for i in range(len(X[0])): 
    #take all rows and loop by i for columns
    X[:, i] = le.fit_transform(X[:, i])
    
print(X)

y = le.fit_transform(y.ravel())
print(y)

#create model
knn = neighbors.KNeighborsClassifier(n_neighbors=25, weights='uniform')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

knn.fit(X_train, y_train)

pred = knn.predict(X_test)

accuracy = metrics.accuracy_score(y_test, pred)
print('Predictions:', pred)
print('Accuracy:', accuracy)

z = 1666
print('Actual Value:', y[z])
print('Predicted Value:', knn.predict(X)[z])

'''
Cross Validation to find best value of k
'''
k_values = [i for i in range(705, 720)]
scores = []

scalar = StandardScaler()
X = scalar.fit_transform(X)

for k in k_values:
    knn = neighbors.KNeighborsClassifier(n_neighbors=k)
    score = cross_val_score(knn, X, y, cv = 5)
    scores.append(np.mean(score))
    
sns.lineplot(x = k_values, y = scores, marker = 'o')
plt.xlabel('K values')
plt.ylabel('Accuracy Scores')
plt.show()

best_index = np.argmax(scores)
best_k = k_values[best_index]

knn = neighbors.KNeighborsClassifier(n_neighbors=best_k)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

accuracy = metrics.accuracy_score(y_test, y_pred)
precision = metrics.precision_score(y_test, y_pred, pos_label='positive',average='micro')
recall = metrics.recall_score(y_test, y_pred, pos_label='positive', average='micro')

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)


