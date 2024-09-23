def TemperatureFluctuationDetection(self, data):
    #Signal
    Signal = 0
    Threshold1 = 10000
    Threshold2 = 1
    #Finding dT for all cells
    arr = []
    for i in range(0,13):
        if i == 0:
            arr.append(data['TS0_FLT'].diff().dropna().reset_index(drop = True))
        else:
            arr.append(data[f'TS{i}'].diff().dropna().reset_index(drop = True))
    arr.append(data['TS13_FLT'].diff().dropna().reset_index(drop = True))

    #Finding dt
    dt = data['Millis'].diff().dropna().reset_index(drop = True)

    #Finding dT/dt
    arr2 = []
    for i in range(0, len(arr)):
        arr2.append(arr[i]/dt)

    #Finding std for all temperatures of the cells
    arr3 = []
    for i in range(0, len(arr2)):
        STD_VALUE = np.std(arr2[i])
        arr3.append(STD_VALUE*Threshold1)

    #Finding the maximum std value
    if max(arr3) > Threshold2:
        Signal = Signal + 1

    return Signal