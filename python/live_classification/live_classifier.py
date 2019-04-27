
#!/usr/bin/env python3
# This File uses the pickled svm to classify motions
import pickle
import sklearn as sk
import pickle
import sys
import time

from sklearn import svm
from liveloader import loadData
from pandas import DataFrame

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
    input()

    # Parse input
    while True:
        # collect Data over time period
        timer = time.monotonic()
        data = []

        while time.monotonic() - timer < 1.5: 
            data.append(input())

        data = loadData(data)

        # Classify
        data = convert_data(data)

        collist = data.columns.tolist()

        print(model.predict(data[collist[:-1]]))

def convert_data(raw_data):
    data = []

    for data_file in raw_data:
        row = []
        data_file[1].extend(data_file[2])
        for x in data_file[1]:
            for y in x:
                row.extend([y])

        row.append(":D")
        data.append(row)
        
    data = DataFrame(data)
    return data


if __name__ == "__main__":
    main()
