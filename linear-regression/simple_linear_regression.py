#Simples Linear Regression

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Import the Dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :1].values
y = dataset.iloc[:, 1].values


#Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0) 

#Feature Scaling
'''from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)'''

#Fitting Simple Linear Regression to the Training test
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train )

#Predicting the Test set results
y_pred = regressor.predict(X_test)