import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

'''
%matplotlib inline
It means, the plot/graph will be displayed directly 
below the cell 
(where the plotting commands are written) 
and the resulted plot/graph will also be included 
(stored) in your notebook document
'''

#import dataset and extract dependent and independent variables
salary_data = pd.read_csv('ML algorithms\Salary_Data.csv')
'''
.iloc[:, :-1].values
all rows and all columns except last one
.iloc[:, 1].values
all rows and only the first column
'''
X = salary_data.iloc[:, :-1].values
y = salary_data.iloc[:, 1].values
print(X)
print(y)

#visualizing the dataset
sns.kdeplot(salary_data['YearsExperience'])
plt.show()
sns.displot(salary_data['YearsExperience'])
plt.show()
sns.countplot(y='YearsExperience', data=salary_data)
plt.show()
sns.barplot(x='YearsExperience', y='Salary', data=salary_data)
plt.show()
sns.heatmap(salary_data.corr())
plt.show()

#splitting into training set and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.33, random_state=0)
#test size = 0.33 /33%
#random state

#fitting simple linear regression to the training set
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train, y_train)

#predicting test results
y_pred = lr.predict(X_test)
print(y_pred)
#y_test model will predict hence we dont pass it here

#visualizing the Training set results
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Salary ~ Experience (Train set)')
plt.scatter(X_train, y_train, color = 'blue')
plt.plot(X_train, lr.predict(X_train), color = 'red')
plt.show()

#visualizing the Test set results
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Salary ~ Experience (Test set)')
plt.scatter(X_test, y_test, color='blue')
plt.plot(X_train, lr.predict(X_train), color='red')
plt.show()

#max accuracy = least error
#measuring the residuals/errors
from sklearn import metrics
print('MAE:', metrics.mean_absolute_error(y_test, y_pred))
print('MSE:', metrics.mean_squared_error(y_test, y_pred))
print('RMSE:', np.sqrt(metrics.mean_absolute_error(y_test, y_pred)))





