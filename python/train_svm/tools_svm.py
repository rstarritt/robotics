import numpy as np
import pandas as pd
import sklearn as sk

from scipy.stats import norm
from pandas import DataFrame
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
    train , test = train_test_split(data)

    # Fit SVM
    collist = data.columns.tolist()
    # you can now select from this list any arbritrary range

    model = svm.SVC(gamma=.1, C=10)
    model.fit(train[collist[:-1]], train[collist[-1]])

    #print(cross_val_score(model, data[collist[:-1]], data[collist[-1]],cv = 5))

    c_parms = [0.1, 0.25, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
    g_parms = [0.001, 0.01, 0.1, 1]

    parms = {'C': c_parms, 'gamma': g_parms}

    model = GridSearchCV(svm.SVC(), parms, cv=10)  
    model.fit(train[collist[:-1]], train[collist[-1]])
  
    print('Training accuracy:', model.best_score_)
    print('Best parameters:', model.best_params_)

    #confusion matrix
    print("\nConfusion Matrix")
    print(confusion_matrix(test[collist[-1]], model.predict(test[collist[:-1]])))

    #classification report
    print("\nClassification Report")
    print(classification_report(test[collist[-1]], model.predict(test[collist[:-1]])))

    # return tested svm
    return model

def classify_svm(data, SVM):
    pass