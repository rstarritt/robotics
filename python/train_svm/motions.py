#!/usr/bin/env python3

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
    lowvrange = ((1.3, 1.6),(0.9, 1.4))
    trange = ((0.8, 1.2), (0.2, 0.6))

    # file format: x y z x y z ...
    # joint order: head, lhand, rhand, baseSpine

    with open(filename) as f:
        for l, i in enumerate(f):
            return False
        


def wellfordsavg(prev, x_n, n):
    return prev + (x_n - prev) / n