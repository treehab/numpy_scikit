import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

dataset = pd.read_csv('ML algorithms\SocialNetworkAds.csv')

#extracting datset 
X = dataset.iloc[:, [2,3]].values
y = dataset.iloc[:, 4].values

print(X)
print(y)

#visualizing  dataset with correlation variables
sns.heatmap(dataset.corr())
plt.show()

#splitting dataset into Training and Testing data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

'''
Feature Scaling
normalize range of independent variables or features of data
performed in data preprocessing step
used in case there is huge variation of values in dataset, it helps improve accuracy
types -
Normalization
Standardization
'''
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

#fitting logistics regression to training dataset
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)
#fit is for training, both x and y values are used

#predicting test results
y_pred = classifier.predict(X_test)
print(y_pred)
#predict is for testing, only x value is called, y is predicted
#now we compare the y_pred with y_test in next few steps

#visualizing Training set results
from matplotlib.colors import ListedColormap
X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(np.arange(start = X_set[:,0].min()-1, stop = X_set[:,0].max()+1, step = 0.01),
                     np.arange(start = X_set[:,1].min()-1, stop = X_set[:,1].max()+1, step = 0.01))
#contour predicts change in Z values as compared to X and Y values
#contourf plots contour colours

plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
#set x limits of the current axes
plt.ylim(X2.min(), X2.max())
#set y limits of the current axes

'''
iteration - repetition/generate a sequence of outcomes
enumerate - keep a count of iterations
'''
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j,0], X_set[y_set == j,1],
                c = ListedColormap(('red','green'))(i), label = j)
plt.title('Logistic Regression (Training Set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()
#green -> class 1
#red -> class 0
#misclassification is shown

#visualizing Test Set
X_set, y_set = X_test, y_test
X1, X2 = np.meshgrid(np.arange(start=X_set[:, 0].min()-1, stop=X_set[:, 0].max()+1, step=0.01),
                     np.arange(start=X_set[:, 1].min()-1, stop=X_set[:, 1].max()+1))
# contour predicts change in Z values as compared to X and Y values
# contourf plots contour colours

plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha=0.75, cmap=ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
# set x limits of the current axes
plt.ylim(X2.min(), X2.max())
# set y limits of the current axes

for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c=ListedColormap(('red', 'green'))(i), label=j)
plt.title('Logistic Regression (Test Set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()

#confusion matrix for evaluation
#gives accuracy
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
print(cm)
#89/100 = 90% accuracy