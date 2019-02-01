import unittest
import pointSet

class TestPointSet(unittest.TestCase):


  def test_calcDist(self):
    TEST_FILE = 'test_data/test_data.csv'
    testPointSet = pointSet.PointSet()
    testPointSet.loadData(TEST_FILE)
    self.assertEqual(157.27478863265398, testPointSet.getDistance(testPointSet.pointSet[0], testPointSet.pointSet[1]))


  def test_checkDist(self):
      TEST_FILE = 'test_data/test_data.csv'
      testPointSet = pointSet.PointSet()
      testPointSet.loadData(TEST_FILE)
      self.assertEqual(5, testPointSet.getLength())
      testPointSet.setDistances()
      self.assertEqual(4, testPointSet.getLength())


  def test_getMAD(self):
    TEST_FILE = 'test_data/test_data.csv'
    testPointSet = pointSet.PointSet()
    testPointSet.loadData(TEST_FILE)
    testPointSet.setDistances()
    self.assertEqual(0.04789525410973283, testPointSet.getMAD())


  def test_checkTimes(self):
    TEST_FILE = 'test_data/test_data.csv'
    testPointSet = pointSet.PointSet()
    testPointSet.loadData(TEST_FILE)
    # with bad timestamps
    testPointSet.removeTimeErrors()
    self.assertEqual(5, testPointSet.getLength())
    
    TEST_TIME_FILE = 'test_data/test_timedata.csv'
    testTimeSet = pointSet.PointSet()
    testTimeSet.loadData(TEST_TIME_FILE)
    # without timestamps
    testTimeSet.removeTimeErrors()
    self.assertEqual(2, testTimeSet.getLength())


  def test_removeOutliers(self):
    TEST_FILE = 'test_data/test_data.csv'
    testPointSet = pointSet.PointSet()
    testPointSet.loadData(TEST_FILE)
    testPointSet.removeOutliers()
    testPointSet.printDetails()
    self.assertEqual(3, testPointSet.getLength())

if __name__ == '__main__':
    unittest.main()