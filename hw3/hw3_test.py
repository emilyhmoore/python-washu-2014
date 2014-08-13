import unittest

from hw3 import *

class SortingTest(unittest.TestCase):
	def test_bubblesort(self):
		self.assertEqual([1,2,3], bubblesort([2,1,3]))
		self.assertEqual([-10,-1,2,5,7], bubblesort([5,2,7,-10,-1]))
		self.assertEqual([0], bubblesort([0]))

	def test_mergesort(self):
		self.assertEqual([1,2,3,4], mergesort([4,2,3,1]))
		self.assertEqual([-10,1,5,8,10,95,100,1000], mergesort([1,5,-10,10,95,100,1000,8]))

if __name__ == '__main__':
	unittest.main()
		