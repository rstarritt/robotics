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
    return DataFrame()

# Train and return SVM
def train_svm(data):
    # Get dataframe
    data = convert_data(data)

    # Train test split

    # Fit SVM
    
    # return tested svm
    return svm.SVC(kernel='linear', C=10)


def classify_svm(data, SVM):
    pass