# Main entry point for the python code
import sys
import sklearn as sk
import tools_svm
import pickle

from data_reader import get_data
from sklearn import svm

def main(argv):
    if len(argv) <= 0:
        print("Usage: python3 main.py training_file1 ... trainingfile_n")
        exit(-1)

    print("Reading Data files")
    data = []
    for x in argv:
        data.append(get_data(x))

    # Train SVM
    print("Training SVM")
    trained = tools_svm.train_svm(data)

    # Pickle it for later
    with open("trained.obj", "wb") as pickle_file:
        pickle.dump(trained, pickle_file)

    print("SVM Stored")


if __name__ == "__main__":
    main(sys.argv[1:])