def ordinal(n):
	last_digit = n% 100
	second_to_last_digit = (n% 100)/10
	if second_to_last_digit == 1:
		ending="th"
	elif last_digit == 1:
		ending= "st"
	elif last_digit == 2:
		ending= "nd"
	elif last_digit == 3:
		ending "rd"
	else:
		ending="th"
	return str(n) + ending