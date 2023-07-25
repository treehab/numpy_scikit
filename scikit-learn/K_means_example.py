from sklearn.datasets import load_breast_cancer
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import scale
import pandas as pd
import numpy as np

bc = load_breast_cancer()
print(bc)

X = scale(bc.data)
print(X)

y = bc.target
print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

model = KMeans(n_clusters=2, random_state=0)
#randomization in algorithm changes everytime but setting it to an arbitrary number generalizes it

model.fit(X_train)
print(model)

predictions = model.predict(X_test)
print(model)

labels = model.labels_

#otherwise it gives low accuracy

#cross validation test
print(pd.crosstab(y_train, labels))
print('Labels:', labels)
print('Predictions', predictions)
print('Accuracy:', accuracy_score(y_test, predictions))
print('Actual Values:', y_test)

'''
still gives low accuracy,
accuracy score may not be directly comparable to the 
accuracy score obtained using a supervised learning 
algorithm trained for classification like SVM, 
Naive Bayes, Random Forest, etc. 
because the clustering algorithm is not designed for 
classification tasks
'''

from sklearn import metrics
def bench_k_means(estimator, name, data):
    estimator.fit(data)
    print('%-9s\t%i\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f'
        % (name, estimator.inertia_,
          metrics.homogeneity_score(y, estimator.labels_),
          metrics.completeness_score(y, estimator.labels_),
          metrics.v_measure_score(y, estimator.labels_),
          metrics.adjusted_rand_score(y, estimator.labels_),
          metrics.adjusted_mutual_info_score(y,  estimator.labels_),
          metrics.silhouette_score(data, estimator.labels_,
                                   metric='euclidean')))


print(bench_k_means(model, "1", X))

print(pd.crosstab(y_train, labels))
