
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


def plot_learning_curve(clf, title, X, y, ylim=None, kf=None,
                        n_jobs=1, train_sizes=np.linspace(.1, 1.0, 5)):
    train_sizes, train_scores, test_scores = learning_curve(
        clf, X, y, cv=kf)
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)

    plt.figure()
    plt.title(title)
    plt.xlabel("Training examples")
    plt.ylabel("Score")
    plt.gca().invert_yaxis()

    # box-like grid
    plt.grid()

    # plot the std deviation as a transparent range at each training set size
    plt.fill_between(train_sizes, train_scores_mean - train_scores_std, train_scores_mean + train_scores_std,
                     alpha=0.1, color="r")
    plt.fill_between(train_sizes, test_scores_mean - test_scores_std, test_scores_mean + test_scores_std,
                     alpha=0.1, color="g")

    # plot the average training and test score lines at each training set size
    plt.plot(train_sizes, train_scores_mean, 'o-', color="r", label="Training score")
    plt.plot(train_sizes, test_scores_mean, 'o-', color="g", label="Cross-validation score")
    plt.legend()

    # sizes the window for readability and displays the plot
    # shows error from 0 to 1.1
    plt.ylim(-.1, 1.1)
    # plt.savefig('learning_curve')
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: python testlearner.py <filename>"
        sys.exit(1)
    inf = open(sys.argv[1])


    # if "sensor_readings_" in inf.name:
    #     data = np.array([s.strip().split(',') for s in inf.readlines()])
    #     dataX = data[:, 0:-1]
    #     dataY = data[:, -1]
    #     dataY[dataY == "Sharp-Right-Turn"] = 1
    #     dataY[dataY == "Slight-Right-Turn"] = 2
    #     dataY[dataY == "Move-Forward"] = 3
    #     dataY[dataY == "Slight-Left-Turn"] = 4
    #     dataY = dataY.astype(float)
    #
    # else:
    data = np.array([map(float, s.strip().split(',')) for s in inf.readlines()])
    dataX = data[:, 0:-1]
    dataY = data[:, -1]

    # if "winequality" in inf.name:
    # categorize wine quality
    # df = pd.DataFrame(data,
    #                   columns=['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides',
    #                            'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates',
    #                            'alcohol', 'quality'])
    # print df['quality'].value_counts()
    # bins = (2.5, 5.5, 9.5)
    # group_names = ['bad', 'good']
    # categories = pd.cut(df['quality'], bins, labels=group_names)
    # df['quality'] = categories
    # data = df.as_matrix()
    # dataX = data[:, 0:-1]
    # dataY = data[:, -1]
    # # le = LabelEncoder()
    # # dataY = le.fit_transform(dataY)
    # dataY[dataY == "good"] = 1
    # dataY[dataY == "bad"] = 2
    dataY[dataY < 5.5] = 0
    dataY[dataY >= 5.5] = 1
    dataY = dataY.astype(float)
    dataX = scale(dataX)
    dataX = np.round(dataX, decimals=3)
    data = np.column_stack((dataX,dataY))
    np.savetxt('Data/winequality-white-modified.csv', data, delimiter=',', fmt='%s')

    # # Training test split
    #
    # trainX, testX, trainY, testY = train_test_split(dataX, dataY, test_size=0.20)
    #
    # scaler = StandardScaler()
    # trainX = scaler.fit_transform(trainX)
    # testX = scaler.transform(testX)
    #
    # trainX, valX, trainY, valY = train_test_split(trainX, trainY, test_size=0.20)
    #
    # # Initialize
    # hidden_layer_sizes = (100,)
    # activation = 'relu'
    # alpha = 0.0001
    # max_iter = 200
    # solver = 'adam'
    # batch_size = 'auto'
    # learning_rate = 'constant'
    # learning_rate_init = 0.001
    # clf = MLPClassifier(max_iter=max_iter, alpha=alpha, hidden_layer_sizes=hidden_layer_sizes,
    #                     activation=activation, solver=solver, batch_size=batch_size,
    #                     learning_rate_init=learning_rate_init)
    #
    # layer_units = None
    # clf._initialize(trainY, layer_units)
    # #Training
    #
    # start_time = time.time()
    # clf.fit(trainX, trainY)
    # end_time = time.time()
    # print('Training complete in %0.5f seconds ...' % (end_time - start_time))
    #
    # k_value = 5
    # kf = KFold(n_splits=k_value)
    # scores = cross_val_score(clf, valX, valY, cv=kf)
    # print "Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() / 2)
    #
    #
    # ##### PLOT LEARNING CURVE #########
    # plot_learning_curve(clf, "Classifier", valX, valY, kf=kf)
    # print('Cross-validation complete...')
    #
    #
    #
    # start_time = time.time()
    # output = clf.predict(testX)
    # end_time  = time.time()
    #
    # print('Completed testing in %0.5f seconds' % (end_time-start_time))
    # # rmse_out = sqrt(mean_squared_error(testY, output))
    # accuracy = accuracy_score(testY, output)
    # # precision = precision_score(testY, output, average='macro')
    # # recall = recall_score(testY, output, average='macro')
    # print "Accuracy: %0.2f" % (accuracy)
    # # print 'Precision: %0.2f' % (precision)
    # # print 'Recall: %0.2f' % (recall)
    # # print 'RMSE: {}'.format(rmse_out)
    # print(classification_report(testY, output))
    #
    #
    # ####### PRINT CONFUSION MATRIX #########
    #
    # cm = confusion_matrix(testY, output)
    # sns.heatmap(cm, annot=True, fmt='2.0f')
    # plt.show()
    # # plt.savefig('confusion_matrix')
