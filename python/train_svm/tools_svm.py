import numpy as np
import pandas as pd
import sklearn as sk

from scipy.stats import norm
from pandas import Series, DataFrame

from sklearn import svm

# SVM is constructed accordinf to following slides
# http://inside.mines.edu/~hzhang/Courses/CSCI473-573/Lectures/07-RobotLearning.pdf

# Get data into a useful data frame
def convert_data(raw_data):
    data_frames = None
    for data_folder in raw_data:
        histograms = []

        for data_file in data_folder[1]:
            pass

        classifier = data_folder[0]
        #data_frames.append([DataFrame("pose": data_folder[0])])


    return DataFrame()

# Train and return SVM
def train_svm(data):
    # Get dataframe
    data = convert_data(data)

    # Train test split

    # Fit SVM
    model = svm.SCV()
    model.fit(data[['x','y']], data['class'])
    # return tested svm
    return svm.SVC(kernel='linear', C=10)


def classify_svm(data, SVM):
    pass