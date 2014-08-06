class School():
	def __init__(self,name):
		self.name=name
		self.db={}
	def add(self, student, grade):
		student_set=set()
		student_set.update([student])
		self.db[grade]=student_set #creats a set
		