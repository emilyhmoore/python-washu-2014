class Bob():
	def __init__(self):
		pass
	
	@classmethod
	def askbob(self, txt):
		is_question = "?" in txt
		answer="Whatever"
		if is_question:
			answer="Sure."
		if txt==txt.upper():
			answer="Whoah, chill out!"
		#if txt == ("")
		#	answer="Fine. Be that way!"
		return answer