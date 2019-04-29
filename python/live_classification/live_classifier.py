
#!/usr/bin/env python3
# This File uses the pickled svm to classify motions
import pickle
import sklearn as sk
import pickle
import sys
import time
import subprocess
import random
from gtts import gTTS
import os

from sklearn import svm
from liveloader import loadData
from pandas import DataFrame

# This expects a stream of data from the astra software
# through a pipe into stdin.

dances = {'GBB' : ('Go Big Blue', 5), 'csm' : ('C S M', 5), 
          'defence' : ('defence', 2.5), 'highV' : ('high V', 2), 
          'lowV' : ('Low V', 2), 't' : ('T', 2)}

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
    print(model.classes_)

    # Parse input
    while True:
        # Random dance, move
        dance = random.choice(model.classes_)
        print(dance)
        print(dances[dance][0])

        tts = gTTS(text=dances[dance][0], lang='en')
        tts.save("dance.mp3")
        subprocess.check_output(["mpv", "dance.mp3"])

        # collect Data over time period
        timer = time.monotonic()
        data = []

        while time.monotonic() - timer < dances[dance][1]: 
            data.append(input())

        data = loadData(data)

        # Classify
        data = convert_data(data)

        collist = data.columns.tolist()

        classification = model.predict(data[collist[:-1]])

        time.sleep(3)

        if dances[classification[0]] == dances[dance]:
            tts = gTTS(text="Good", lang='en')
            tts.save("dance.mp3")
            subprocess.check_output(["mpv", "dance.mp3"])
        else:
            tts = gTTS(text="Bad, Try again", lang='en')
            tts.save("dance.mp3")
            subprocess.check_output(["mpv", "dance.mp3"])



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
