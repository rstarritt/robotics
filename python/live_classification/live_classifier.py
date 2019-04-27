
#!/usr/bin/env python3
# This File uses the pickled svm to classify motions
import pickle
import sklearn as sk
import pickle

from sklearn import svm

# This expects a stream of data from the astra software
# through a pipe into stdin.

def main():
    # Load pickle (get trained SVM)
    svm = None
    try:
        with open("./trained.obj", "rb") as pickle_file:
            svm = pickle.load(pickle_file)
    except FileNotFoundError:
        print("No trained SVM found. Please train one!")
        exit(-1)
    
    # Get rid of usb input  warning  
    print(input())

    # Parse input
    while True:
        print(input())

        # Classify
        print("I don't know atm")

if __name__ == "__main__":
    main()