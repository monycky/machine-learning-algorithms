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