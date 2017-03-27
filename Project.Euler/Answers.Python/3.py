# Problem 3
# https://projecteuler.net/problem=3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Libao Jin
# March 15, 2015

def Factor(n):

	factors = []
	divisor = 2
	while divisor <= n:
		if n % divisor == 0:
			factors.append(divisor)
			n = n / divisor
		else:
			if divisor == 2:
				divisor += 1
			else:
				divisor += 2
	return factors

f = Factor(600851475143)
f = Factor(2)
print f

	
