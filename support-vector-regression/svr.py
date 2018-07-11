#SVR

#Import the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Import the Dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

#Splitting the dataset into the Training set and Test set
'''from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0) '''

#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y) 


#Fitting the SVR to the dataset
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X, y)

#Create your regressor here

#Predicting a new result 
y_pred = regressor.predict(6.5)


#Visualising the SRV
plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('Truth or Bluff (SRV Results)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()


