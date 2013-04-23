from SpiralPrint import spiralPrinter
import unittest

class TestSpiralPrint(unittest.TestCase):
  
  def testEmptyMatrix(self):
    self.assertEqual('', spiralPrinter([[]]))
    
  def testNormalMatrix(self):
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9,10,11,12]]
    self.assertEqual('1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7', spiralPrinter(matrix))
    
  def testNotConsistentMatrix(self):
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9,10,11,12]]
    self.assertRaises(Exception, spiralPrinter(matrix))
    
  def testSingleElement(self):
    matrix = [[1]]
    self.assertEqual('1', spiralPrinter(matrix))
    
if __name__ == '__main__':
  unittest.main() 