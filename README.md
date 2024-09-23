# Temperature-Fluctuation-Algorithm
<br>
Temperature Fluctuation Algorithm is designed to detect any kind of fluctuations in the Thermister Sensor used for measuring the temperature of different areas in battery pack (Near cells). 
<br>
Fluctuations in the Sensor can be caused due to various reasons :
<br>
1. Loosening of Connectors.
<br>
2. Thermister Sensor wiring pinching.
<br>
3. Female and Male wire of Thermister short due to various reasons (Either Dead Short or Earthening)
<br>
<br>
Following are the descriptions of the Algorithm
<br>
1. Version 1.0.0
<br>
The concept that was used to built this agorithm is using Rate of Change of Temperature with Time. The Intution behind using rate of change is that, as the sensor shows more fluctutations, there is more rate of change of the temperature and setting a threshold for the same will help in detect the fluctuations.
<br>
Working : 
<br>
1. Find Rate of Change of Temperature with time for all sensors.
<br>
2. Find the Standard Deviation of the Rate of Change for all sensors.
<br>
3. Set a threshold. If Standard Deviation exceeds the threshold value, There is a Probability of Temperature Fluctuation.
<br>
<br>
2. Version 2.0.0
<br>
The concept used to built this algorithm is different from Version 1.0.0. To detect the fluctuations, we used the deviation of original Temperature data from the Moving Average Filter data. As the fluctuation increases the deviation also increases. 
<br>
Working :
<br>
1. Mean Centering of the data of all Temperature Sensors.
<br>
2. Find the Moving Average of all Temperature Sensors.
<br>
3. Find the deviation of Original data with Moving Average for all Temperature Sensors.
<br>
4. Find the Variance of the deviation for all Temperature Sensors.
<br>
5. Set a threshold. If Variance exceeds the threshold value, There is a Probability of Temperature Fluctuation.
<br>
Improvements :
<br>
1. Comparatively less False Positives. 