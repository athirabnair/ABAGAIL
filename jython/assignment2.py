
import sys
from re import match

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from id3 import Id3Estimator
from sklearn import tree
from sklearn.ensemble import AdaBoostClassifier
from sklearn.linear_model import Perceptron
from sklearn.metrics import *
from sklearn.model_selection import KFold, train_test_split, learning_curve, cross_val_score, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler, scale
from sklearn.svm import SVC
import time
import csv

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: python testlearner.py <filename>"
        sys.exit(1)
    inf = open(sys.argv[1])


    data = np.array([map(float, s.strip().split(',')) for s in inf.readlines()])
    dataX = data[:, 0:-1]
    dataY = data[:, -1]

    dataY[dataY < 5.5] = 0
    dataY[dataY >= 5.5] = 1
    dataY = dataY.astype(float)
    dataX = scale(dataX)
    dataX = np.round(dataX, decimals=3)
    data = np.column_stack((dataX,dataY))
    np.savetxt('Data/winequality-white-modified.csv', data, delimiter=',', fmt='%s')
