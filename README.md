# Soapbox Test Code 


**Author:** Patrick Concannon

**Problem:** Develop an algorithm that, given a series of data
points (latitude,longitude,timestamp) for a car journey from
A->B, which will disregard potentially erroneous points
(present in #the dataset).

**Date Modified:** 31 Jan, 2019

## Code Description

When approaching this problem I decided to begin by first looking at the timestamps. With the assumption that during the journey the time would always be increasing, I filtered out points with timestamps that did not follow consecutively. Next, I looked for 'zero distances', or distances between the latitude and longitude points that equated to zero, as this would indicate potentially erroneous or duplication of data-points. Following this I moved on to looking at removing any outlying points that might indicate a bad data-point. For this I originally looked at getting the mean distance between points and then checking each point against the standard deviation from this mean or average. While this worked well, the method was very suspetible to large outliers that would skew the mean and standard deviation. With this in mind I decided to use the Absolute Median Deviation(MAD) instead -- as it was less susceptible to the effect of large outlying points.
From here I found the median distance travelled between the points +/- the Median Deviation from it. This provided a consistent set of points that formed a path between A and B. However, in order to get the largest catchment of correct points I referred to the Chebyshev's Theorem (discussed below)  and increased the percentage deviation from the median. To increase the accurate further, I plotted the points to give me a better picture of which points where far from the path and this let me rework how large or small the Chebyshev constant should be e.g. how far to deviate from the median. 

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
