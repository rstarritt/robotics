import numpy as np
import pandas as pd
import sklearn as sk

from scipy.stats import norm
from pandas import Series, DataFrame
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
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
    print(data)
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

    # Test
    score = model.score(test[collist[:-1]], test[collist[-1]])
    print(f"model score: {score}")

    #setup to get f-score and cv
    #scorerVar = make_scorer(f1_score, pos_label=1)
    #scores = cross_val_score(model, boat[["Pclass", "Age", "Pclass", "Fare"]], boat["Survived"],cv = 5, scoring = scorerVar)
    #print(f"Cross Validation f1_score: {scores.mean()}")

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