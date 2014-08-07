class School():
	def __init__(self,name):
		self.name=name
		self.db={}
	
	def add(self, student, grade):
		student_set=set()
		if self.db.has_key(grade):
			student_set=self.db[grade]
		student_set.add(student)
		self.db[grade]=student_set
		return self.db
	
	def grade(self, grade):
		if self.db.has_key(grade):
			return self.db[grade]	
		else:
			return None
	
	def sort(self):
		sorted_students=[]
		for i in range(len(sorted(self.db))):
			sorted_students.append(tuple(self.db[sorted(self.db)[i]])) ##make a list of the students in order
		sorted_db=dict(zip(sorted(self.db),sorted_students)) ##zip them into a dictionary
		return sorted_db
			