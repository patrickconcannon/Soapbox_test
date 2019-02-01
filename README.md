# Soapbox Test Code 


**Author:** Patrick Concannon

**Problem:** Develop an algorithm that, given a series of data
points (latitude,longitude,timestamp) for a car journey from
A->B, which will disregard potentially erroneous points
(present in #the dataset).

**Date Modified:** 31 Jan, 2019


All Formulas referenced from: 
-  http://www.ltcconline.net/greenl/courses/201/descstat/mean.htm
-  https://www.statisticshowto.datasciencecentral.com/median-absolute-deviation/
 
-  Median Absolute Derivation(MAD) used as it is
  as it is more robust to outliers than standard deviation.

-  Chebyshev's Theorem uses a constant k to tell us that at 
  least k%  of data lies within k%  of the Median. By increasing
  and decreasing it it will allow control over the optimal deviation
  in distance between points
  
**Files**: 
1. main.py
2. point.py
3. pointSet.py
4. pointSet_test.py

5. data/ -- original data_points.csv file, which contains lat, long, and timestamp of points in journey
6. graphs/ -- images of graph print out. Organised by timestamp
7. test_data/ -- test data point files used in pointSet_test.py
