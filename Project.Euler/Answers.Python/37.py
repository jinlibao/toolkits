# problem 37
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

def rightTruncateNumber(number):
	string = str(number)
	rightTruncatedNumbers = []
	for i,e in enumerate(string):
		if i == 0:
			tstring = string[:]
		else:
			tstring = string[:-(i)]
		#print(string, tstring)
		rightTruncatedNumbers.append(int(tstring))
	return rightTruncatedNumbers

def leftTruncateNumber(number):
	string = str(number)
	leftTruncatedNumbers = []
	for i,e in enumerate(string):
		tstring = string[i:]
		leftTruncatedNumbers.append(int(tstring))
	return leftTruncatedNumbers

def isTruncatablePrimes(number):
	rightTruncatedNumbers = rightTruncateNumber(number)
	leftTruncatedNumbers = leftTruncateNumber(number)
	isTruncatable = []
	for i in rightTruncatedNumbers:
		isTruncatable.append(isPrime(i))
	for i in leftTruncatedNumbers:
		isTruncatable.append(isPrime(i))
	if all(isTruncatable):
		return True
	else:
		return False

def truncatablePrimes():
	tPrimes = []
	number = 11
	numberOfTPrimes = len(tPrimes)
	while numberOfTPrimes < 11:
		if isTruncatablePrimes(number):
			print(number)
			tPrimes.append(number)
		number += 2
		numberOfTPrimes = len(tPrimes)
	sumTPrimes = sum(tPrimes)
	return (sumTPrimes, tPrimes)

def solution():
	tPrimes = truncatablePrimes()
	print(tPrimes)

def test():
	number = 12345
	print(rightTruncateNumber(number))
	print(leftTruncateNumber(number))

solution()
#test()
