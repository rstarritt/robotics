#!/usr/bin/env python3
import time
from math import atan2
# hardcode angles
# will be given file from astra of raw xyz. (can probably call stuff from Sam's code)
# will be given motion name
# last 10 frames, average positions? calculate angles based on averages
# compare averages to hardcoded angles
# will be called as a function

__name__ = "motions"

def correctMotion(filename, motionname):
    # ((thetaMin, thetaMax),(phiMin,phiMax))
    highVrange = ((0.35, 0.6),(0.2, 0.6))
    lowVrange = ((1.3, 1.6),(0.9, 1.4))
    trange = ((0.8, 1.2), (0.2, 0.6))

    # file format: x y z x y z ...
    # joint order: head, lhand, rhand, baseSpine
    joint0avg = [0, 0, 0]
    joint4avg = [0, 0, 0]
    joint7avg = [0, 0, 0]
    joint9avg = [0, 0, 0]
    linecount = 0
    with open(filename) as f:
        for i in f:
            linecount += 1
            i = i.strip()
            tokens = i.split(' ')
            for token, val in enumerate(tokens):
                tokens[token].rstrip()
                # print(tokens[token], ' ' , token)
                if float(token) < 3:
                    joint0avg[token%3] = wellfordsavg(joint0avg[token%3], float(val), linecount)
                if float(token) <= 3 and float(token) < 6:
                    joint4avg[token%3] = wellfordsavg(joint4avg[token%3], float(val), linecount)
                if float(token) <= 6 and float(token) < 9:
                    joint7avg[token%3] = wellfordsavg(joint7avg[token%3], float(val), linecount)
                if float(token) <= 9 and float(token) < 12:
                    joint9avg[token%3] = wellfordsavg(joint9avg[token%3], float(val), linecount)

    print(joint0avg[0])

    # calculate angles
    angles = []
    angles.append(getTheta(joint0avg, joint4avg, joint7avg, joint9avg))
    angles.append(getPhi(joint0avg, joint4avg, joint7avg, joint9avg))

    # truthTable has every condition for the angles being in range
    truthTable = [False, False, False, False, False, False, False, False]
    instructions = ""
    # determine if angles are correct
    if motionname is "High V":
        # if theta in range and phi in range, return correct, else return fail reason
        # thetaR (angles[0][1]) is negatives
        if angles[0][0] >= highVrange[0][0]:
            truthTable[0] = True
        if angles[0][0] <= highVrange[0][1]:
            truthTable[1] = True
        if angles[0][1] <= 0 - highVrange[0][0]:
            truthTable[2] = True
        if angles[0][1] >= 0 - highVrange[0][1]:
            truthTable[3] = True
        if angles[1][0] >= highVrange[1][0]:
            truthTable[4] = True
        if angles[1][0] <= highVrange[1][1]:
            truthTable[5] = True
        if angles[1][1] >= highVrange[1][0]:
            truthTable[6] = True
        if angles[1][1] <= highVrange[1][1]:
            truthTable[7] = True
        # go over truthTable, and append string as required
    elif motionname is "Low V":
         # if theta in range and phi in range, return correct, else return fail reason
        # thetaR (angles[0][1]) is negatives
        if angles[0][0] >= lowVrange[0][0]:
            truthTable[0] = True
        if angles[0][0] <= lowVrange[0][1]:
            truthTable[1] = True
        if angles[0][1] <= 0 - lowVrange[0][0]:
            truthTable[2] = True
        if angles[0][1] >= 0 - lowVrange[0][1]:
            truthTable[3] = True
        if angles[1][0] >= lowVrange[1][0]:
            truthTable[4] = True
        if angles[1][0] <= lowVrange[1][1]:
            truthTable[5] = True
        if angles[1][1] >= lowVrange[1][0]:
            truthTable[6] = True
        if angles[1][1] <= lowVrange[1][1]:
            truthTable[7] = True
    elif motionname is "T":
        # if theta in range and phi in range, return correct, else return fail reason
        # thetaR (angles[0][1]) is negatives
        if angles[0][0] >= trange[0][0]:
            truthTable[0] = True
        if angles[0][0] <= trange[0][1]:
            truthTable[1] = True
        if angles[0][1] <= 0 - trange[0][0]:
            truthTable[2] = True
        if angles[0][1] >= 0 - trange[0][1]:
            truthTable[3] = True
        if angles[1][0] >= trange[1][0]:
            truthTable[4] = True
        if angles[1][0] <= trange[1][1]:
            truthTable[5] = True
        if angles[1][1] >= trange[1][0]:
            truthTable[6] = True
        if angles[1][1] <= trange[1][1]:
            truthTable[7] = True

    if not truthTable[0]:
        instructions += "Raise left arm. "
    if not truthTable[1]:
        instructions += "Lower left arm. "
    if not truthTable[2]:
        instructions += "Raise right arm. "
    if not truthTable[3]:
        instructions += "Lower right arm. "
    if not truthTable[4]:
        instructions += "Move left arm forwards. "
    if not truthTable[5]:
        instructions += "Move left arm back. "
    if not truthTable[6]:
        instructions += "Move right arm forwards. "
    if not truthTable[7]:
        instructions += "Move right arm back. "
    # check if instructions is empty. if so, return correct
    if instructions is "":
        return "Correct"
    return instructions

def wellfordsavg(prev, x_n, n):
    return prev + (x_n - prev) / n

def getTheta(head, left_hand, right_hand, hip):
    thetaL = (atan2(left_hand[1] - hip[1], left_hand[0] - hip[0]) - atan2(head[1] - hip[1], head[0] - hip[0]))
    thetaR = (atan2(right_hand[1] - hip[1], right_hand[0] - hip[0]) - atan2(head[1] - hip[1], head[0] - hip[0]))
    return (thetaL, thetaR)

def getPhi(head, left_hand, right_hand, hip):
    phiL = (atan2(left_hand[1] - hip[1], left_hand[2] - hip[2]) - atan2(head[1] - hip[1], head[2] - hip[2]))
    phiR = (atan2(right_hand[1] - hip[1], right_hand[2] - hip[2]) - atan2(head[1] - hip[1], head[2] - hip[2]))
    return (phiL, phiR)