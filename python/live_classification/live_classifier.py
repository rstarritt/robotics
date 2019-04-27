
#!/usr/bin/env python3
# This File uses the pickled svm to classify motions
import pickle
import sklearn as sk
import pickle
import sys

from sklearn import svm
from liveloader import loadData

# This expects a stream of data from the astra software
# through a pipe into stdin.

def main():
    # Load pickle (get trained SVM)
    model = None
    try:
        with open("./trained.obj", "rb") as pickle_file:
            model = pickle.load(pickle_file)
    except FileNotFoundError:
        print("No trained SVM found. Please train one!")
        exit(-1)
    
    # Get rid of usb input  warning  
    print(input())

    # Parse input
    while True:
        # collect Data over time period
        raw = input()
        print(raw)

        # Classify
        print("I don't know atm")
        #model.predict("berg")

if __name__ == "__main__":
    main()