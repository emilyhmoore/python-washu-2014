class Bob():
	def __init__(self):
		pass
	
	def askbob(self, txt):
		is_question = "?" in txt
		answer="Whatever"
		if is_question:
			answer="Sure."
		if txt==txt.upper(txt):
			answer="Whoah, chill out!"
		return answer
	
		