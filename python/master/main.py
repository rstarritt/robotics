import sys
import os, signal
import subprocess
import time
import random
sys.path.append('../train_svm/')
from motions import correctMotion

def main():
    s=subprocess.call("exec " + "../../flite-2.1-release/bin/./flite -voice rms -t \"would you like to play a game?\"", shell = True)
    time.sleep(1)
 #   rm=subprocess.call("rm test.txt", shell = True)
 #   s2=subprocess.call("../../samples/bin/./BodyReaderPoll ../../python/master/test.txt", shell = True, timeout = 1)

    motions = ["High V", "Low V", "T"]
    

    while True:
        motion = motions[random.randint(0,2)]
        print(motion)
        s3=subprocess.call("exec " + f'../../flite-2.1-release/bin/./flite -voice rms -t "{motion}"', shell = True)
        print(s3)
        data = []
        trimmeData = []
        with open("test.txt","r") as f:
            for l in f:
                data.append(l);
        for i in range (len(data)-190,len(data)):
            tokens = data[i].split('   ')
            if(int(tokens[1]) == 0 or int(tokens[1]) == 4 or int(tokens[1]) == 7 or int(tokens[1]) == 9):
                trimmeData.extend([float(tokens[2]),float(tokens[3]),float(tokens[4])])
                if(int(tokens[1]) == 9):
                    trimmeData.append('\n')
            
        print(trimmeData)
        f = open("../train_svm/finalData.txt", 'w')
        for i in trimmeData:
            if i != '\n':
                f.write(str(i)+ ' ')
            else:
                f.write(str(i))
        result = correctMotion("finalData.txt", motion)
        if result == False:
            s4=subprocess.call("exec " + "../../flite-2.1-release/bin/./flite -voice rms -t \"Incorrect\"", shell = True)
        else:
            s4=subprocess.call("exec " + "../../flite-2.1-release/bin/./flite -voice rms -t \"Correct\"", shell = True)
# allows for command line usage as exacutable
if __name__ == "__main__":
    main()