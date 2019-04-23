import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn as sk

from scipy.stats import norm
from pandas import Series, DataFrame
from matplotlib.colors import ListedColormap

from sklearn import svm

# SVM is constructed accordinf to following slides
# http://inside.mines.edu/~hzhang/Courses/CSCI473-573/Lectures/07-RobotLearning.pdf

# Get data into a useful data frame
def convert_data(raw_data):
    pass

# Train and return SVM
def train_svm(data):
    # Train test split
    pass
    return svm.SVC(kernel='linear', C=10)


def classify_svm(data, SVM):
    pass