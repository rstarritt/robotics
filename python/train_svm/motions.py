#!/usr/bin/env python3
import time
# hardcode angles
# will be given file from astra of raw xyz. (can probably call stuff from Sam's code)
# will be given motion name
# last 10 frames, average positions? calculate angles based on averages
# compare averages to hardcoded angles
# will be called as a function

def correctMotion(filename, motionname):
    # ((thetaMin, thetaMax),(phiMin,phiMax))
    highVrange = ((0.35, 0.6),(0.2, 0.6))
    lowvrange = ((1.3, 1.6),(0.9, 1.4))
    trange = ((0.8, 1.2), (0.2, 0.6))

    # file format: x y z x y z ...
    # joint order: head, lhand, rhand, baseSpine
    joint0 = []
    joint4 = []
    joint7 = []
    joint9 = []
    with open(filename) as f:
        for i in f:
            i = i.strip()
            tokens = i.split(' ')
            for token in range(0,len(tokens)):
                tokens[token].rstrip()
                print(tokens[token], ' ' , token)
                if float(token) < 3:
                    joint0.append(tokens[token])
                if float(token) <= 3 and float(token) < 6:
                    joint4.append(tokens[token])
                if float(token) <= 6 and float(token) < 9:
                    joint7.append(tokens[token])
                if float(token) <= 9 and float(token) < 12:
                    joint9.append(tokens[token])
            
    print(joint0)


def wellfordsavg(prev, x_n, n):
    return prev + (x_n - prev) / n