#!/usr/bin/env python3
import os
from math import sqrt, acos

# Loads data from data set 
def loadData(data, bin_dist=7, bin_angle=7):

    # Open train and test
    return processFolder(data, bin_dist, bin_angle)

def processFolder(data, bin_dist, bin_angle):

    results = []

    rads = []

    frames = processData(data)
    for x in frames:
        rads.extend([Rad(x)])

    # histograms for d1
    dist_min = [x * float('inf') for x in range(5)] #[1,2,3,4,5,6,n]
    dist_max = [x * float('-inf') for x in range(5)]
    ang_min  = [x * float('inf') for x in range(5)]
    ang_max  = [x * float('-inf') for x in range(5)]
    
    # Find info for range sizes
    for rad_frame in rads:
        # Find maxes and mins
        for i in range(len(rad_frame.joints)):
            joint = rad_frame.joints[i]
            if joint[0] < dist_min[i]:
                dist_min[i] = joint[0]
            elif joint[0] > dist_max[i]:
                dist_max[i] = joint[0]
            
            if joint[1] < ang_min[i]:
                ang_min[i] = joint[1]
            elif joint[1] > ang_max[i]:
                ang_max[i] = joint[1]

    # Get Counts
    bin_dist_count  = [x * 0 for x in range(5)]
    bin_angle_count  = [x * 0 for x in range(5)]

    # Split into bins
    for i in range(len(rad_frame.joints)):
        range_size_dist = (dist_max[i] - dist_min[i]) / bin_dist
        range_size_ang  = (ang_max[i]  - ang_min[i] ) / bin_angle

        bin_dist_ranges = [(x * range_size_dist + dist_min[i], x * range_size_dist + dist_min[i] + range_size_dist) for x in range(bin_dist)]
        bin_ang_ranges  = [(x * range_size_ang  +  ang_min[i], x * range_size_ang  + ang_min[i]  + range_size_ang ) for x in range(bin_angle)]
        
        bin_dist_count[i]  = [x * 0 for x in range(bin_dist)]
        bin_angle_count[i] = [x * 0 for x in range(bin_angle)]
        
        for rad_frame in rads:
            joint_to_be_counted = rad_frame.joints[i]
            for x in range(bin_dist):
                if joint_to_be_counted[0] > bin_dist_ranges[x][0] and joint_to_be_counted[0] < bin_dist_ranges[x][1]:
                    bin_dist_count[i][x] += 1
                    break
            for x in range(bin_angle):
                if joint_to_be_counted[1] > bin_ang_ranges[x][0] and joint_to_be_counted[1] < bin_ang_ranges[x][1]:
                    bin_angle_count[i][x] += 1
                    break

    # Normalize distances
    for x in range(len(bin_dist_count)):
        for y in range(bin_dist):
            bin_dist_count[x][y] = bin_dist_count[x][y] / len(rads)

    # Normalize Angles
    for x in range(len(bin_angle_count)):
        for y in range(bin_angle):
            bin_angle_count[x][y] = bin_angle_count[x][y] / len(rads)

    # Add to Results
    results.append(["Live", bin_dist_count[1::], bin_angle_count[1::]])

    return results

# returns a list of frames
def processData(data):
    frames = []
    for i in range(len(data)):
        if (len(data) - i) < 18:
            break
        if int(data[i].split()[1]) != 0:
            continue

        curFrame = []
        curFrame.extend([RawJoint(data[i])])

        for _ in range(18):
            i += 1
            try:
                curFrame.extend([RawJoint(data[i])])
            except:
                print(i % 18)
    
        frames.append(curFrame)

    return frames

# Class for joint data
class RawJoint:
    def __init__(self, raw_string):
        data = raw_string.split()
        self.frame = int(data[0])
        self.jointID = int(data[1])
        self.joint_position_x = float(data[2])
        self.joint_position_y = float(data[3])
        self.joint_position_z = float(data[4])
        self.Coords = (self.joint_position_x,self.joint_position_y,self.joint_position_z)

# Class for Frame data
class Rad:
    def __init__(self, frame):
        self.raw = frame

        # [Dist to center, Angle, Coordinates]
        self.head = [None, None, None]
        self.left_hand = [None, None, None]
        self.left_foot = [None, None, None]
        self.right_hand = [None, None, None]
        self.right_foot = [None, None, None]
        self.hip = [None, None, None]
        self.joints = (
            self.head,
            self.left_hand,
            self.left_foot,
            self.right_hand,
            self.right_foot,
        )

        # See: include/astra/capi/streams/body_types.h
        """
        ASTRA_JOINT_HEAD              = 0,
        ASTRA_JOINT_SHOULDER_SPINE    = 1,
        ASTRA_JOINT_LEFT_SHOULDER     = 2,
        ASTRA_JOINT_LEFT_ELBOW        = 3,
        ASTRA_JOINT_LEFT_HAND         = 4,
        ASTRA_JOINT_RIGHT_SHOULDER    = 5,
        ASTRA_JOINT_RIGHT_ELBOW       = 6,
        ASTRA_JOINT_RIGHT_HAND        = 7,
        ASTRA_JOINT_MID_SPINE         = 8,
        ASTRA_JOINT_BASE_SPINE        = 9,
        ASTRA_JOINT_LEFT_HIP          = 10,
        ASTRA_JOINT_LEFT_KNEE         = 11,
        ASTRA_JOINT_LEFT_FOOT         = 12,
        ASTRA_JOINT_RIGHT_HIP         = 13,
        ASTRA_JOINT_RIGHT_KNEE        = 14,
        ASTRA_JOINT_RIGHT_FOOT        = 15,
        ASTRA_JOINT_LEFT_WRIST        = 16,
        ASTRA_JOINT_RIGHT_WRIST       = 17,
        ASTRA_JOINT_NECK              = 18,
        ASTRA_JOINT_UNKNOWN           = 255,
        """
        star = {
            0  : self.head,
            4  : self.left_hand,
            11 : self.left_foot,
            7  : self.right_hand,
            14 : self.right_foot,
            9  : self.hip
        }

        # Get Key Joints
        for x in frame:
            if x.jointID in star:
                star[x.jointID][2] = x.Coords

        center = star[9]
            
        first = True
        for key, joint in star.items():
            if key is 9:
                continue
            joint[0] = self.getDist(center[2], joint[2])

        for key, joint in star.items():
            if key is 9:
                continue
            if first:
                last_joint = self.left_hand
                first = False
            joint[1] = self.getAngle(last_joint, joint, center)
            last_joint = joint 

    def getDist(self, start, finish):
        return sqrt((start[0] - finish[0]) ** 2 + (start[1] - finish[1]) ** 2 + (start[2] - finish[2]) ** 2)

    def getAngle(self, start, finish, center): #(x, y, z)
        dot = 0
        for x in range(3):
            dot += (finish[2][x] - center[2][x]) * (start[2][x]- center[2][x])
        # print (f"dot {dot}, {dot / (start[0] * finish[0])}")
        return acos(dot / (start[0] * finish[0]))