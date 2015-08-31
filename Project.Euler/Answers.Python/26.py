# problem 26
# Project Euler

__author__ = 'Libao Jin'
__date__ = 'July 18, 2015'

def decimalPart(number):
	pass

def fractionValue(number):
	return 1 / number

def isRecurring(number):
	pass

def reciprocalCycles(UpperBound):
	numbers = list(range(1, UpperBound))
	for n in numbers:
		fraction = fractionValue(n)
		#decimalValue = decimalPart(fraction)
		print('{0:.100f}'.format(fraction))

def solution():
	reciprocalCycles(1000)

solution()
# unfinished
