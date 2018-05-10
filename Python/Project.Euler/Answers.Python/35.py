# problem 35
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

def rotateDigits(number):
	string = str(number)
	rotatedString = string[::-1]
	rotatedNumber = int(rotatedString)
	return rotatedNumber

def isCircularPrime(number):
	if isPrime(number):
		rotatedNumber = rotateDigits(number)
		if isPrime(rotatedNumber):
			return True
	return False

def circularPrimes(UPPER_BOUND):
	cPrimes = [2,3]
	number = 5
	while number < UPPER_BOUND:
		#print(number)
		if isCircularPrime(number):
			cPrimes.append(number)
		number += 2
	numberOfCPrimes = len(cPrimes)
	return (numberOfCPrimes, cPrimes)

def solution():
	UPPER_BOUND = 1000000
	cPrimes = circularPrimes(UPPER_BOUND)
	print(cPrimes)

def test():
	number = 123456
	rotatedNumber = rotateDigits(number)
	print((number, rotatedNumber))

solution()
