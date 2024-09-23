import os
import pandas as pd
import numpy as np
import seaborn as sns
import math
import matplotlib.pyplot as plt
%matplotlib inline

def moving_average(data, window_size):
    return data.rolling(window=window_size).mean()

def Function(TS_FILE_DF):
    #Signal Initialization
    Signal = 0
    SensorWithIssue = None
    #Sensor Names
#     TempArrays = ['TS1', 'TS2', 'TS3', 'TS4', 'TS5', 'TS6', 'TS7', 'TS8', 'TS9', 'TS10', 'TS11', 'TS12', 'TS0_FLT', 'TS13_FLT']
    TempArrays = ['ts1', 'ts2', 'ts3', 'ts4', 'ts5', 'ts6','ts7', 'ts8', 'ts9', 'ts10', 'ts11', 'ts12', 'ts0_flt', 'ts13_flt']
    #Parameters
    ThresholdValv1 = 0.0011
    ThresholdValv2 = 0.0025
    WindowThreshold = 20
    #FeatureFetching
    TS_FILE_DF = TS_FILE_DF[TempArrays]
    #Mean Centering
    TS_FILE_DF = TS_FILE_DF - TS_FILE_DF.mean()
    #Moving average filtered New data
    NewArr = np.array([moving_average(data = TS_FILE_DF[i], window_size = WindowThreshold) for i in TempArrays])
    #OldArr
    OldArr = np.array([np.array(TS_FILE_DF[i]) for i in TempArrays])
    #Old vs New Diff
    DiffArr = OldArr-NewArr
    #Varience Storage
    VarianceStorage = [np.var(DiffArr[i][WindowThreshold-1:]) for i in range(0,len(DiffArr))]
    #Threshold
    for i in range(0,len(VarianceStorage)):
        if i <= 11: #This is the threshold given for temperature sensors 'ts1', 'ts2', 'ts3', 'ts4', 'ts5','ts6', 'ts7', 'ts8', 'ts9', 'ts10', 'ts11', 'ts12'
            if VarianceStorage[i] > ThresholdValv1:
                SensorWithIssue = f"TS{i+1}"
                Signal = Signal + 1
                break
        else:       #This is the threshold given for temperature sensors 'ts0_flt','ts13_flt'
            if VarianceStorage[i] > ThresholdValv2:
                if i == 12:
                    SensorWithIssue = "TS0_FLT"
                    Signal = Signal + 1
                    break
                elif i == 13:
                    SensorWithIssue = "TS13_FLT"
                    Signal = Signal + 1
                    break
    return Signal, SensorWithIssue