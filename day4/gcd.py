def gcd(number1, number2):
	remainder=number1 % number2
	while remainder !=0:
		new_remainder=number2 % remainder
		number2=remainder
		remainder=new_remainder
	return number2
	
print gcd(1071, 462)

def find_primes():
	numbers=range(2,122)
	primes=[]
	while len(numbers)!=0:
		primes.append(numbers[0])
		p=numbers[0]
		for number in numbers:
			if number%p == 0:
				numbers.remove(number)
	return primes
print find_primes()

##Got this from RosettaCode
def hanoi(ndisks, startPeg=1, endPeg=3):
    if ndisks:
        hanoi(ndisks-1, startPeg, 6-startPeg-endPeg)
        print "Move disk %d from peg %d to peg %d" % (ndisks, startPeg, endPeg)
        hanoi(ndisks-1, 6-startPeg-endPeg, endPeg)
 
hanoi(ndisks=4)
	
	
	
	
	
	
	
