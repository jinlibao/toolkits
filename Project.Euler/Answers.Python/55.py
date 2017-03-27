# problem 55
# Project Euler

__author__ = 'Libao Jin'
__date__ = 'July 17, 2015'

def rotateDigits(number):
	string = str(number)
	rotatedString = string[::-1]
	rotatedNumber = int(rotatedString)
	return rotatedNumber

def isSymmetrical(number):
	rotatedNumber = rotateDigits(number)
	if rotatedNumber == number:
		return True
	else:
		return False

def isLychrelNumber(number):
	iterTimes = 0
	rotatedNumber = rotateDigits(number)
	number = number + rotatedNumber
	while iterTimes < 50:
		if isSymmetrical(number):
			return False
		else:
			rotatedNumber = rotateDigits(number)
			number = number + rotatedNumber
			iterTimes += 1
	if iterTimes >= 50:
		return True

def LychrelNumbers(UPPER_BOUND):
	number = 1
	lNumbers = []
	while number < UPPER_BOUND:
		if isLychrelNumber(number):
			lNumbers.append(number)
			number += 1
		else:
			number += 1
	numberOfLychrelNumbers = len(lNumbers)
	return (numberOfLychrelNumbers, lNumbers)

def solution():
	UPPER_BOUND = 10000
	LN_Info = LychrelNumbers(UPPER_BOUND)
	print(LN_Info)

solution()
