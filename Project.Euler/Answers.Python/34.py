# problem 34
# Project Euler

__author__ = 'Libao Jin'
__date__ = 'July 17, 2015'

def extractDigits(number):
	string = str(number)
	digits = []
	for i in string:
		digits.append(int(i))
	return digits

def factorial(n):
	if n <= 1:
		return 1
	product = 1
	while n > 1:
		product *= n
		n -= 1
	return product

def factorialSeries():
	fSeries = []
	for i in range(10):
		if i == 0:
			fSeries.append(1)
		else:
			value = fSeries[i-1] * i
			fSeries.append(value)
	return fSeries
	
def sumFactorialDigits(digits, fSeries):
	number = 0
	for d in digits:
		number += fSeries[d]
		#number += factorial(d)
	return number

def isSpecial(number, fSeries):
	if number <= 2:
		return False
	digits = extractDigits(number)
	sumOfDigits = sumFactorialDigits(digits, fSeries)
	if sumOfDigits == number:
		return True
	else:
		return False

def digitsFactorials(UPPER_BOUND):
	i = 2
	fSeries = factorialSeries()
	specialNumbers = []
	while i < UPPER_BOUND:
		if isSpecial(i, fSeries):
			specialNumbers.append(i)
		i += 1
	return (sum(specialNumbers), specialNumbers)

def recurringNumber(numberOfDigits):
	rNumber = 0
	for i in range(numberOfDigits):
		rNumber += 10 ** i
	return rNumber

def genBOUND():
	numberOfDigits = 2
	a = factorial(9) * numberOfDigits
	b = recurringNumber(numberOfDigits) * 9
	while a > b:
		a = factorial(9) * numberOfDigits
		b = recurringNumber(numberOfDigits) * 9
		numberOfDigits += 1
	return a

def solution():
	BOUND = genBOUND()
	print('Upper bound is {0:d}'.format(BOUND))
	numbers = digitsFactorials(BOUND)
	print(numbers)

solution()
