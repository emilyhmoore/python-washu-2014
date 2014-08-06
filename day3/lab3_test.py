import unittest
import lab3

class Lab3Test(unittest.TestCase):

	def setUp(self):
		pass

	def test_shout_abc(self):
		self.assertEqual("ABC!", lab3.shout("abc")) 
	
	def test_shout_punctuation(self):
		self.assertEqual("CAT!", lab3.shout("cat.")) 
	
	def test_reverse_abc(self):
		self.assertEqual("cba", lab3.reverse("abc"))
		self.assertEqual(".cba", lab3.reverse("abc."))
	
	def test_reversewords(self):
		self.assertEqual("? you hate I", lab3.reversewords("I hate you?"))
		self.assertEqual("! Run", lab3.reversewords("Run!"))
		self.assertEqual(". World Hello", lab3.reversewords("Hello World."))
		self.assertEqual("? you are How . World Hello", lab3.reversewords("Hello World. How are you?"))
	
	def test_reverse_sentence_words(self):
		self.assertEqual("nuR!", lab3.reversewordletters("Run!"))
	
if __name__=='__main__':
	unittest.main()