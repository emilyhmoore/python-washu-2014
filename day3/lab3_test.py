import unittest
import lab3

class Lab3Test(unittest.TestCase):

	def setUp(self):
		pass

	def test_shout_abc(self):
		self.assertEqual("ABC!", lab3.shout("abc")) 

if __name__=='__main__':
	unittest.main