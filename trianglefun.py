def is_triangle (side1, side2, side3):
	if int(side1)>int(side2+side3):
		print "no"
	elif int(side2)>int(side1+side3):
		print "no"
	elif int(side3)>int(side1+side2):
		print "no"
	else: print "yes"

side1=raw_input("How long is side 1?")
side2=raw_input("How long is side 2?")
side3=raw_input("How long is side 3?")

is_triangle(side1,side2,side3)