import unittest
import ordinal

class OrdinalTest(unittest.TestCase):
	def setup(self):
		pass
	def test_first(self):
		self.assertEqual("1st", ordinal.ordinal(1))

if __name__ == '__main__':
	unittest.main()