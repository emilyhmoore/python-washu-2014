import unittest
import teen

class TeenTest(unittest.TestCase):

	def setUp(self):
		pass
	
	def test_sure(self):
		self.assertEqual("Sure.", teen.Bob().askbob("How are you?")) 
	
	#def test_yell(self):
	#	self.assertEqual("Woah, chill out!", teen.

if __name__=='__main__':
	unittest.main()