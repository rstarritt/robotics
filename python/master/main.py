import sys
import os, signal
import subprocess
import time
sys.path.insert(0, '../train_svm')
from motions.py import correctMotion

def main():
    s=subprocess.call("exec " + "../../flite-2.1-release/bin/./flite -voice rms -t \"would you like to play a game?\"", shell = True)
 #   rm=subprocess.call("rm test.txt", shell = True)
 #   s2=subprocess.call("../../samples/bin/./BodyReaderPoll ../../python/master/test.txt", shell = True, timeout = 1)
    while True:
        s3=subprocess.call("exec " + "../../flite-2.1-release/bin/./flite -voice rms -t \"High V\"", shell = True)
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
        result = correctMotion("finalData.txt", "High V")
        if result == False:
            s4=subprocess.call("exec " + "../../flite-2.1-release/bin/./flite -voice rms -t \"Incorrect\"", shell = True)
        else:
            s4=subprocess.call("exec " + "../../flite-2.1-release/bin/./flite -voice rms -t \"Correct\"", shell = True)
# allows for command line usage as exacutable
if __name__ == "__main__":
    main()