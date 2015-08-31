# problem 10
# Project Euler

import math

__author__ = 'Libao Jin'
__date__ = 'July 12, 2015'

def isPrime(n):
	upperBound = math.sqrt(n)

	if n == 2:
		return True

	i = 2
	while i <= upperBound:
		if n % i == 0:
			return False
		else:
			i += 1
	return True

def primesArray(n):
	parray = []
	i = 2
	while i < n:
		if isPrime(i):
			parray.append(i)
			#print(i)
			i += 1
		else:
			i += 1
	return parray

def sumOfPrimes(n):
	parray = primesArray(n)
	sop = sum(parray)
	print(sop)
	return sop
	
N = int(2e6)

print(N, sumOfPrimes(N))
