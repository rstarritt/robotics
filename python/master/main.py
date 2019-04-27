#!/usr/bin/env python3

import sys
import os, signal
import subprocess
import time
import random
sys.path.append('../train_svm/')
from motions import correctMotion

def main():
    subprocess.call("exec " + "flite -voice rms -t \"would you like to play a game?\"", shell = True)
    time.sleep(1)


    motions = ["High V", "Low V", "T"]

    # Make sure that all binaries have been made
    if not os.path.isfile("../../samples/CMakeCache.txt"):
        subprocess.call("cmake ../../samples", shell = True)
        subprocess.call("make", shell = True, cwd="../../samples")
    

    while True:
        motion = motions[random.randint(0,2)]
        # print(motion)

        s3 = subprocess.call("exec " + f'flite -voice rms -t "{motion}"', shell = True)
        #time.sleep(2)
        #if os.path.isfile("rm test.txt"):
            #subprocess.call("rm test.txt", shell = True)
        
        try:
            subprocess.call("../../samples/bin/./BodyReaderPoll ./test.txt", shell = True, timeout = 3)
        except:
            print("Data Read in")
        
        print(s3)
        data = []
        trimmeData = []
        if not os.path.isfile("test.txt"):
            continue
            
        with open("test.txt","r") as f:
            for l in f:
                data.append(l)
        for i in range (len(data)-190,len(data)):
            tokens = data[i].split('   ')
            if(int(tokens[1]) == 0 or int(tokens[1]) == 4 or int(tokens[1]) == 7 or int(tokens[1]) == 9):
                trimmeData.extend([float(tokens[2]),float(tokens[3]),float(tokens[4])])
                if(int(tokens[1]) == 9):
                    trimmeData.append('\n')
            
        #print(trimmeData)
        with open("../train_svm/finalData.txt", 'w') as f:
            for i in trimmeData:
                if i != '\n':
                    f.write(str(i)+ ' ')
                else:
                    f.write(str(i))
        result = correctMotion("../train_svm/finalData.txt", motion)
        subprocess.call("exec " + f'flite -voice rms -t "{result}"', shell = True)
# allows for command line usage as exacutable
if __name__ == "__main__":
    main()