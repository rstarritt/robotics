
# This File uses the pickled svm to classify motions
import pickle
# This expects a stream of data from the astra software
# through a pipe into stdin.

def main():
    pass
    # Load pickle (get trained SVM)
    svm = None
    try:
        with open("../train_svm/trained.obj", "rb") as pickle_file:
            svm = pickle.load(pickle_file)
    except FileNotFoundError:
        print("No trained SVM found. Please train one!")
        exit(-1)
    
    # Get data from stdin
    input()
    # Classify
    print("I don't know atm")

if __name__ == "__main__":
    main()