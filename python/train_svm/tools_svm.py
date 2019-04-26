import numpy as np
import pandas as pd
import sklearn as sk

from scipy.stats import norm
from pandas import Series, DataFrame
from sklearn.model_selection import train_test_split
from sklearn import svm

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
    collist = data.columns.tolist()
    # you can now select from this list any arbritrary range

    model = svm.SVC(gamma=.1, C=10)
    model.fit(data[collist[:-1]], data[collist[-1]])
    # return tested svm
    return model

def classify_svm(data, SVM):
    pass