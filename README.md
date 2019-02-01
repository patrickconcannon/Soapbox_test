# Soapbox Test Code 


**Author:** Patrick Concannon

**Problem:** Develop an algorithm that, given a series of data
points (latitude,longitude,timestamp) for a car journey from
A->B, which will disregard potentially erroneous points
(present in #the dataset).

**Date Modified:** 31 Jan, 2019

## Code Description

To solve this problem I decided to first look at the timestamps. On the assumption that in the journey the time would always be increasing I first filter the data set of points with erroneous timestamps. Next, I looked for zero distance travelled between points as this would indicate potentially erroneous (duplication) points. After this I then looked at removing any outlying points that might indicate an bad point. For this I originally looked at getting the mean distance between points and then checking each point against the standard deviation from this mean or average. While this worked well, this method was very suspetible to large outliers that would skew the mean and standard deviation. With this in mind I decided to use the Absolute Median Deviation(MAD) instead as it was less susceptible to the effect of large outlying points.
From here I found the median distance travelled between the points +/- the Median Deviation from it to the most points that would plot the best possible path. In order to get the largest catchment of correct points I referred to the Chebyshev's Theorem, discussed below, which allows you to increase the deviation from the median. To be as accurate as possible I plotted the points to give me a better idea of how far to deviate from the median. 

The result of this meant I was able to filter out 55 potentially erroneous points leaving 172 from the 227 original data points.

All Formulas referenced from: 
-  http://www.ltcconline.net/greenl/courses/201/descstat/mean.htm
-  https://www.statisticshowto.datasciencecentral.com/median-absolute-deviation/
 
-  Median Absolute Derivation(MAD) used as it is
  as it is more robust to outliers than standard deviation.

-  Chebyshev's Theorem uses a constant k to tell us that at 
  least k%  of data lies within k%  of the Median. By increasing
  and decreasing it it will allow control over the optimal deviation
  in distance between points
  
## Files 
 - main.py
 - point.py
 - pointSet.py
 - pointSet_test.py

 - data/ -- original data_points.csv file, which contains lat, long, and timestamp of points in journey
 - graphs/ -- images of graph print out. Organised by timestamp
 - test_data/ -- test data point files used in pointSet_test.py
