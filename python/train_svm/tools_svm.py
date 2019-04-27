import numpy as np
import pandas as pd
import sklearn as sk

from scipy.stats import norm
from pandas import Series, DataFrame
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn import svm
from sklearn import metrics
from sklearn.metrics import confusion_matrix, f1_score, classification_report, make_scorer
from sklearn import model_selection

# SVM is constructed accordinf to following slides
# http://inside.mines.edu/~hzhang/Courses/CSCI473-573/Lectures/07-RobotLearning.pdf

# Get data into a useful data frame
def convert_data(raw_data):
    data = []

    for folder in raw_data:
        classification = folder[0]

        for data_file in folder[1]:
            row = []
            data_file[1].extend(data_file[2])
            for x in data_file[1]:
                for y in x:
                    row.extend([y])

            row.append(classification)
            data.append(row)
        
    data = DataFrame(data)
    return data

# Train and return SVM
def train_svm(data):
    # Get dataframe
    data = convert_data(data)

    # Train test split
    train , test =train_test_split(data)

    # Fit SVM
    collist = train.columns.tolist()
    # you can now select from this list any arbritrary range

    model = svm.SVC(gamma=.1, C=10)
    model.fit(train[collist[:-1]], train[collist[-1]])

    tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8],
                     'C': [1, 10, 100, 1000]}]

    scores = ['f1-score', 'recall']

    for score in scores:
        print("# Tuning hyper-parameters for %s" % score)
        print()

        clf = GridSearchCV(svm.SVC(C=1), tuned_parameters, cv=5)
        clf.fit(data[collist[:-1]], data[collist[-1]])

        print("Best parameters set found on development set:")
        print()
        print(clf.best_params_)

    # Test
    score = model.score(test[collist[:-1]], test[collist[-1]])
    print(f"model score: {score}")

    #confusion matrix
    print("Confusion Matrix")
    print(confusion_matrix(test[collist[-1]], model.predict(test[collist[:-1]])))

    #classification report
    print("\nClassification Report")
    print(classification_report(test[collist[-1]], model.predict(test[collist[:-1]])))

    # return tested svm
    return model

def classify_svm(data, SVM):
    pass