from point import Point
from statistics import median
from math import sin, cos, sqrt, atan2, radians

import csv
import datetime
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

"""
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
  
"""

CHEBYSHEV_CONST = 10
RAD_EARTH = 6373.0 # approximate radius of earth in km
ZERO_DIST = 0.0


class PointSet:
  def __init__(self):
    self.pointSet = []
    self.distances = []
    self.duplicatePoints = 0
    self.timestampErrors = 0
    self.outlierCount = 0

  # Load points data from file
  def loadData(self, fileName):
    if fileName:
      with open(fileName, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
          self.pointSet.append(Point(float(row[0]),float(row[1]),float(row[2])))


  def _getLength(self):
        return len(self.pointSet)


  # Returns distance between two points
  def _getDistance(self, p1,p2):
    # Convert to radians
    lat1 = radians(p1.lt)
    lon1 = radians(p1.ln)
    lat2 = radians(p2.lt)
    lon2 = radians(p2.ln)

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return RAD_EARTH * c


  # Gets Median Absolute Deviation(MAD)
  def _getMAD(self):
    med_dist = []
    med = median(self.distances) # median
    for d in self.distances:
      med_dist.append(abs(d - med)) # deviation from median

    return median(med_dist)


  # Calculates and stores distances between points
  def _setDistances(self):  
    if self._getLength() == 0:
          return None
    temp = []
    for i in range(0, self._getLength()-1):
      d = self._getDistance(self.pointSet[i], self.pointSet[i+1])
      
      # skip duplicates e.g. points where no distance is covered 
      if (d == ZERO_DIST) and (i+1 != self._getLength()):
        self.duplicatePoints += 1
        continue

      # store distance to next point within Point obj
      self.pointSet[i].distance = d
      # store all distances between points within PointSet
      self.distances.append(d)
      # keep track of valid points
      temp.append(self.pointSet[i])

    self.pointSet = temp[:]

  # Check for timestamps which aren't consecutive
  def _removeTimeErrors(self):
    cur_low = 0
    temp = []
    for pt in self.pointSet:
      current = pt.timestamp
      # skip points with bad timestamp
      if (current < cur_low):
        self.timestampErrors += 1 
        continue
      cur_low = current
      temp.append(pt)

    self.pointSet = temp[:]

  # Remove outlying points
  def removeOutliers(self):
    self._removeTimeErrors()
    self._setDistances()

    # Calculate MAD
    med = median(self.distances)
    ab_med_dev = self._getMAD() * CHEBYSHEV_CONST
    
    # Add starting point
    temp = []
    temp.append(self.pointSet[0])
    for i in range(0, self._getLength()-1):
      if ((med - ab_med_dev) <= self.pointSet[i].distance <= (med + ab_med_dev)):
        temp.append(self.pointSet[i+1])
      else:
        self.outlierCount += 1

    self.pointSet = temp[:]


  def plotPoints(self):
    x = []
    y = []
    for pt in self.pointSet:
      y.append(pt.lt)
      x.append(pt.ln)

    # set plot options
    mpl.use('Agg')
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)

    # plot graph
    #ax.plot(x,y) # comment to remove line from plot 
    plt.scatter(x,y) # comment to remove points from plot
    
    # Save image of graph
    timestamp = datetime.datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    fig.savefig('graphs/Graph-' + timestamp + '.png')
  

  # Print details of algorithm run
  def printDetails(self): # change to printDetails() and add more info
    print("Duplicate points:\t" + str(self.duplicatePoints))
    print("Timestamp errors:\t" + str(self.timestampErrors))
    print("Outliers:\t\t"       + str(self.outlierCount))
    print("\nCurrent count:\t"  + str(self._getLength()) + "/227")
    print("Erroneous points filtered: " + str(227-(self._getLength())))

