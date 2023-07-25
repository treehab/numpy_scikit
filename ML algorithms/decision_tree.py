import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

#importing the dataset
kyphosis = pd.read_csv('ML algorithms\kyphosis.csv')

#extracting independent variable 
X = kyphosis.drop('Kyphosis', axis=1)

#extracting dependent variable
y = kyphosis['Kyphosis']

#visualization
sns.barplot(x='Kyphosis', y='Age', data = kyphosis)
plt.show()
sns.pairplot(kyphosis, hue='Kyphosis', palette='Set1')
plt.show()

plt.figure(figsize=(35,6))
sns.countplot(x='Age', hue='Kyphosis',data=kyphosis, palette='Set1')
plt.show()

#splitting into Training and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)

X = kyphosis.drop('Kyphosis', axis = 1)
y = kyphosis['Kyphosis']

X.head()
X = kyphosis.iloc[:, [1,2,3]].values
print(X)

y.head()
print(y)

#DECISION TREE TRAINING
from sklearn.tree import DecisionTreeClassifier
dtree = DecisionTreeClassifier()
dtree.fit(X_train, y_train)

#predicting model
dtree_preds = dtree.predict(X_test)
print(dtree_preds)

#evaluate model using classification report and confusion matrix
from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(y_test, dtree_preds))
print(confusion_matrix(y_test, dtree_preds))
#16/27 = 59% accuracy

#RANDOM FOREST
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=100)
rfc.fit(X_train, y_train)

#predicting model
rfc_preds = rfc.predict(X_test)
print(rfc_preds)

#evaluate model using classification report 
from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(y_test, rfc_preds))
print(confusion_matrix(y_test, rfc_preds))
#19/27 = 70% accuracy 