class BiologicalThing(object):
	def alive(self):
		return True
	
class Animal(BiologicalThing):
	def gets_energy_directly_from_the_sun(self):
		return False
		
class Mammal(Animal):
	def _init_(self, age, sex)
		Animal._init_(self, age)
		self.sex=sex
		
	def has_hair(self):
		return True
		
	def has_live_births(self):
		return True

class Human(Mammal): #class definition
	def _init_(self), age, sex, name: #initializer or constructor
	Mammal._init_(age, sex)
	self.name = name
	
	def speak(self, words):
		if self.sex=="Male":
			return words.upper()
		else:
			return words
			
			
	def introduce (self):
		return self.speak("Hello, I'm %s" % self.name)
	
	def reveal_age(self):
		if self.sex=="Male":
			return self.speak("I'm %d" % self.age)
		else:
			return "Don't you know better?"

andy = Human(21, "male", "Andy")
		