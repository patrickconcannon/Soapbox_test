import pointSet

def main():
  CSV_FILE = 'data/data_points.csv'
  ps = pointSet.PointSet()
  ps.loadData(CSV_FILE)
  ps.removeOutliers() 
  ps.plotPoints() 
  ps.printDetails()

if __name__ == '__main__':
    main()
