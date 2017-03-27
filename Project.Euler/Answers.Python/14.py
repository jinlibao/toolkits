# problem 14
# Project Euler

__author__ = 'Libao Jin'
__date__ = 'July 13, 2015'

def isEven(n):
	if n % 2 == 0:
		return True
	else:
		return False

def collatzTransform(n):
	if isEven(n):
		n = n // 2
	else:
		n = 3 * n + 1
	return n

def CollatzSequence(startNumber):
	collatzSeq = [startNumber]
	transformedNumber = collatzTransform(startNumber)
	collatzSeq.append(transformedNumber)
	while transformedNumber != 1:
		transformedNumber = collatzTransform(transformedNumber)
		collatzSeq.append(transformedNumber)
	return [startNumber, len(collatzSeq), collatzSeq]

def longestCollatzStartNumber(UpperBound):
	currentStartNumber = 3
	currentMaxStartNumber = currentStartNumber
	currentMaxLength = 0
	longestCollatzSeq = 0

	while currentStartNumber < UpperBound:
		ccs = CollatzSequence(currentStartNumber)
		if currentMaxLength < ccs[1]:
			currentMaxLength = ccs[1]
			currentMaxStartNumber = ccs[0]
		currentStartNumber += 1
	lcs = CollatzSequence(currentMaxStartNumber)
	return lcs

def test1():
	cs = CollatzSequence(13)
	print(cs)

def test2():
	lcs = longestCollatzStartNumber(1000000)
	print(lcs)

test2()
