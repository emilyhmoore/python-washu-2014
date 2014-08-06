import unittest
import ordinal

class OrdinalTest(unittest.TestCase):
	
	def setup(self):
		pass
		
	def test_first(self):
		self.assertEqual("1st", ordinal.ordinal(1))
	
	def test_second(self):
		self.assertEqual("2nd", ordinal.ordinal(2))
	
	def test_third(self):
		self.assertEqual("3rd", ordinal.ordinal(3))

if __name__ == '__main__':
	unittest.main()