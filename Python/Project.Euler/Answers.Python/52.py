# problem 52
# Project Euler

__author__ = 'Libao Jin'
__date__ = 'July 18, 2015'

def number2digits(number):
	string = str(number)
	digits = []
	for s in string:
		digits.append(int(s))
	return sorted(digits)

def hasSameDigits(number1, number2):
	digits1 = number2digits(number1)
	digits2 = number2digits(number2)
	if digits1 == digits2:
		return True
	else:
		return False

def multiplesOfNumber(number, n):
	times = range(1, n+1)
	multiples = []
	for i in times:
		multiple = number * i
		multiples.append(multiple)
	return multiples

def isQualified(number, n):
	multiples = multiplesOfNumber(number, n)
	
	sameDigits = []
	for m in multiples:
		sameDigits.append(hasSameDigits(number, m))
	if all(sameDigits):
		return True
	else:
		return False

def permutedMultiples(n):
	number = 1
	while not isQualified(number, n):
		number += 1
	pMultiple = multiplesOfNumber(number, n)
	return (number, pMultiple)

def solution():
	number = permutedMultiples(2)
	print(number)

solution()

