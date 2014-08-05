class Parent():
	def _init_(self, sex, firstname, lastname):
		self.sex = sex
		self.firstname=firstname
		self.lastname=lastname
	
	def role(self):
		if self.sex=="Male"
			return "Father"
		else:
			return "Mother"
			
	def have_child(self):
	 print self.firstname + "is having a child"
	 print "They will make a very good" + self.role()
	 child = Child(name, self)
	 self.kids.append(child)
	 
	 
class Child():
	def _init_(self, firstname, parent):
	self.parents = parent
	self.lastname=parent.lastname
	self.firstname=firstname
	
def introduce(self):
	return "Hi I'm %s %s" %(self.firstname, self.lastname)

mom=Parent("Female", "Jane", "Smith")