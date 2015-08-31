# Problem 1
# https://projecteuler.net/problem=1
# If we list all the natural numbers below 10 that are multiples of 3
# or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find
# the sum of all the multiples of 3 or 5 below 1000.

# Libao Jin
# March 15, 2015

def genSeq(n):
	r = range(n+1)
	s = []
	for i in r:
		if i % 5 == 0 or i % 3 == 0:
			s.append(i)	
	return s

s = genSeq(1000)
print s
print sum(s)
