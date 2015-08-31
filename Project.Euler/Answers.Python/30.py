# problem 30
# Project Euler

__author__ = 'Libao Jin'
__date__ = 'July 18, 2015'

def extractDigits(number):
	string = str(number)
	digits = []
	for i in string:
		digits.append(int(i))
	return digits

def sumPowerDigits(digits, n):
	number = 0
	for d in digits:
		number += d ** n
	return number

def isSpecial(number, n):
	digits = extractDigits(number)
	sumOfDigits = sumPowerDigits(digits, n)
	if sumOfDigits == number:
		return True
	else:
		return False

def digitsNthPower(UPPER_BOUND, numberOfPower):
	i = 2
	specialNumbers = []
	while i < UPPER_BOUND:
		if isSpecial(i, numberOfPower):
			specialNumbers.append(i)
		i += 1
	return (sum(specialNumbers), specialNumbers)

def recurringNumber(numberOfDigits):
	rNumber = 0
	for i in range(numberOfDigits):
		rNumber += 10 ** i
	return rNumber

def genBOUND(numberOfPower):
	numberOfDigits = 2
	a = (9 ** (numberOfPower)) * numberOfDigits
	b = recurringNumber(numberOfDigits) * 9
	while a > b:
		a = (9 ** (numberOfPower)) * numberOfDigits
		b = recurringNumber(numberOfDigits) * 9
		numberOfDigits += 1
	return a

def solution():
	numberOfPower = 5
	BOUND = genBOUND(numberOfPower)
	print('Upper bound is {0:d}'.format(BOUND))
	numbers = digitsNthPower(BOUND, numberOfPower)
	print(numbers)

solution()
