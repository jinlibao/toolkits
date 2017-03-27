# Problem 5
# https://projecteuler.net/problem=5
# 
# 2520 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?
# 
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

def SmallestMultiple(n):

	factors = []
	factorCounter = [0 for i in range(n)]
	m = 1
	for i in range(n):
		factors.append(Factor(i+1))
	print factors
	for i in range(n):
		for j in range(n):
			if factors[i].count(j+1) > factorCounter[j]:
				factorCounter[j] = factors[i].count(j+1)
	print factorCounter
	for i in range(n):
		m *= (i+1) ** factorCounter[i]
	return m

sm = SmallestMultiple(20)
print sm
