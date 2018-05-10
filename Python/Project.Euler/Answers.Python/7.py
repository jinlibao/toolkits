# Problem 7
# https://projecteuler.net/problem=7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# 
# What is the 10 001st prime number?
# 
# Libao Jin
# March 15, 2015

import math

def findNthPrime(n):
	
	i = 2
	currentPrime = 3

	if n == 1:
		return 2
	elif n == 2:
		return 3

	while i < n:
		currentPrime += 2
		if isPrime(currentPrime):
			i += 1
	return currentPrime

def isPrime(n):
	
	if n % 2 == 0:
		return False

	for i in range(3, n / 2, 2):
		if n % i == 0:
			return False
	return True

print findNthPrime(10001)
