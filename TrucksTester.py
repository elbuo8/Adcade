from Trucks import paradeScheduler
import unittest
  
class TestTrucks(unittest.TestCase):
  
  #120 generated permutations
  def testPermutationsOf5(self):
    trucks = open('./trucks5')
    result = open('./resulttrucks5')
    self.assertEqual(result.read(), paradeScheduler(trucks))
    result.close()
    trucks.close()
  
  #1 2 3 4 5
  def testSortedTrucks(self):
    trucks = open('./sortedTrucks')
    self.assertEqual('yes', paradeScheduler(trucks))
    trucks.close()  
  
  #5 4 3 2 1
  def testReverseTrucks(self):
    trucks = open('./reverseTrucks')
    self.assertEqual('yes', paradeScheduler(trucks))
    trucks.close()  
  
  #Exit on first iteration
  def testNoTrucks(self):
    trucks = open('./emptyTrucks')
    self.assertEqual('', paradeScheduler(trucks))
    trucks.close()     
  #3
  #1 2 3 4
  def testInconsistentTrucks(self):
    trucks = open('./inconsistentTrucks')
    with self.assertRaises(Exception):
      paradeScheduler(trucks)
    trucks.close()       
    
if __name__ == '__main__':
  unittest.main() 