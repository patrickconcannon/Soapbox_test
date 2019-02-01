Author: Patrick Concannon

Problem: Develop an algorithm that, given a series of data
points (latitude,longitude,timestamp) for a car journey from
A->B, which will disregard potentially erroneous points
(present in #the dataset).

Date Modified: 31 Jan, 2019


All Formulas referenced from: 
-  http://www.ltcconline.net/greenl/courses/201/descstat/mean.htm
 
-  Median Absolute Derivation(MAD) used as it is
  as it is more robust to outliers than standard deviation.

-  Chebyshev's Theorem uses a constant k to tell us that at 
  least k%  of data lies within k%  of the Median. By increasing
  and decreasing it it will allow control over the optimal deviation
  in distance between points