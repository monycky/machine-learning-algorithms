# -*- coding: utf-8 -*-

#Data Preprocessing

#Import the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Import the Dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

#Taking care of missing data
from sklearn.preprocessing import Imputer 
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:,  1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

#Enconding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelenconder_X = LabelEncoder()
X[:, 0] = labelenconder_X.fit_transform(X[:, 0])

oneHotEncoder = OneHotEncoder(categorical_features = [0])
X = oneHotEncoder.fit_transform(X).toarray()

labelenconder_y = LabelEncoder()
y = labelenconder_y.fit_transform(y)

#Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0) 