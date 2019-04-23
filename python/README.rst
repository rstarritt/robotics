How to use
==========

1. Goto the train_svm directory
#. Run ``./main.py data``
#. Then goto live_classification
#. ``./cbin | ./main.py``

What Everything Is
==================

train_svm
---------

This is the folder where our training data and scripts live.
the SVM training scripts must be run **BEFORE** runting the live
scripts.

Data file structure:

- data/data_set_name/data.txt


live_classification
-------------------

The Python script that processes the live data from the astra
sensor lives here.

examples
--------

This folder has the example code for our SVM classification. These
files are jupyter notebooks, for information on how to view these
read the README.txt in that folder

Dependencies
============
- Python >= 3.7
- Scikit Learn
- Pandas
- Numpy
