# problem 27
# Project Euler

import math

__author__ = 'Libao Jin'
__date__ = 'July 18, 2015'

def isPrime(n):
	if n < 0:
		return None
	if n == 1:
		return None
	elif n > 1 and n <= 3:
		return True
	UPPER_BOUND = math.sqrt(n)
	i = 2
	while i <= UPPER_BOUND:
		if n % i != 0:
			i += 1
		else:
			return False
	return True

def quadraticPrimes(a,b):
	qPrimes = []
	n = 0
	number = n ** 2 + a * n + b
	while isPrime(number):
		qPrimes.append((n, number))
		n += 1
		number = n ** 2 + a * n + b
	return ((a,b), len(qPrimes), qPrimes)

def bruteForce(BOUND_a, BOUND_b):
	aSeries = range(-BOUND_a, BOUND_a+1)
	bSeries = range(-BOUND_b, BOUND_b+1)
	currentMAX = -1
	MAX = None
	for a in aSeries:
		for b in bSeries:
			qPrimesInfo = quadraticPrimes(a,b)
			if qPrimesInfo[1] > currentMAX:
				currentMAX = qPrimesInfo[1]
				MAX = qPrimesInfo
	return MAX

def solution():
	MAX = bruteForce(1000, 1000)
	maxProduct = MAX[0][0] * MAX[0][1]
	print(MAX, maxProduct)

def test():
	for i in range(1,100):
		print('{0:d}:'.format(i), isPrime(i))

solution()
