How to use
==========

#. Run ``cd install; sudo ./install.sh``
#. Add the specified lines to your bashrc
#. Go back to root directory
#. Run ``cd python; pipenv shell``
#. Run ``pipenv sync``
#. Run ``cd live_classification; ./run.sh``

What Everything Is
==================

python/train_svm
----------------

This is the folder where our training data and scripts live.
the SVM training scripts must be run **BEFORE** runting the live
scripts. This is done automatically in the run.sh script.

Data file structure:

- data/data_set_name/data.txt


python/live_classification
--------------------------

The Python script that processes the live data from the astra
sensor lives here. It uses the trained SVM to classify movements

python/examples
---------------

This folder has the example code for our SVM classification. These
files are jupyter notebooks, for information on how to view these
read the README.txt in that folder

Dependencies
============
- Python >= 3.7
   - Scikit Learn
   - SciPy
   - Pandas
   - Numpy
   - gTTS
- pipenv
- mpv
