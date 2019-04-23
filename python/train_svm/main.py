# Main entry point for the python code
import sys
import os
import sklearn as sk
import tools_svm
import pickle

from loader import loadData
from sklearn import svm

def main(argv):
    if len(argv) != 1:
        print("Usage: python3 main.py folder_with_datasets")
        exit(-1)
    try:
        for x in os.listdir(argv[0]):
            print(x)
            if argv[0][-1] == "/":
                data = loadData(argv[0] + x)
            else:
                data = loadData(argv[0] + '/' +x)

    except FileNotFoundError:
        print("That is not a valid directory")
        exit(-1)

    print(data)

    # Train SVM
    print("Training SVM")
    trained = tools_svm.train_svm(data)

    # Pickle it for later
    with open("trained.obj", "wb") as pickle_file:
        pickle.dump(trained, pickle_file)

    print("SVM Stored")


if __name__ == "__main__":
    main(sys.argv[1:])