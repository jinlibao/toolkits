# problem 35_hack
# Project Euler

import math

__author__ = 'Libao Jin'
__date__ = 'July 17, 2015'

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

def primeSeries(UPPER_BOUND):
	pSeries = [2, 3]
	number = 5
	while number < UPPER_BOUND:
		if isPrime(number):
			pSeries.append(number)
		number += 2
	print('pSeries has been generated.')
	return pSeries

def isPrimeHack(n, pSeries):
	if pSeries.__contains__(n):
		return True
	else:
		return False

def rotateDigits(number):
	string = str(number)
	rotatedString = string[::-1]
	rotatedNumber = int(rotatedString)
	return rotatedNumber

def isCircularPrimeHack(number, pSeries):
	if isPrimeHack(number, pSeries):
		rotatedNumber = rotateDigits(number)
		if isPrimeHack(rotatedNumber, pSeries):
			return True
	return False

def circularPrimesHack(UPPER_BOUND):
	pSeries = primeSeries(UPPER_BOUND)
	cPrimes = [2,3]
	number = 5
	while number < UPPER_BOUND:
		#print(number)
		if isCircularPrimeHack(number, pSeries):
			cPrimes.append(number)
		number += 2
	numberOfCPrimes = len(cPrimes)
	return (numberOfCPrimes, cPrimes)

def solution():
	UPPER_BOUND = 1000000
	cPrimes = circularPrimesHack(UPPER_BOUND)
	print(cPrimes)

def test():
	number = 123456
	rotatedNumber = rotateDigits(number)
	print((number, rotatedNumber))

solution()
