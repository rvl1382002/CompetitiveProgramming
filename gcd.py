# Author: Riddhish V. Lichade
# username: root_rvl

def computeGCD(x, y):
	while(y):
	    x, y = y, x % y
	return abs(x)

# prints 12
print ("The gcd of 60 and 48 is : ",end="")
print (computeGCD(48,60))
