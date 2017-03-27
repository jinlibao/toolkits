# problem 29
# Project Euler

__author__ = 'Libao Jin'
__date__ = 'July 18, 2015'

def power(a, b):
	p = a ** b
	return p

def matrix2list(matrix):
	newList = []
	for m in matrix:
		for i in m:
			newList.append(i)
	return newList

def distinctPowers2(LOWER_BOUND, UPPER_BOUND):
	aSeries = range(LOWER_BOUND, UPPER_BOUND+1)
	bSeries = range(LOWER_BOUND, UPPER_BOUND+1)
	pSeries = []
	for i,a in enumerate(aSeries):
		for j,b in enumerate(bSeries):
				pSeries.append(a ** b)
	pSet = sorted(set(pSeries))
	pSetLength = len(pSet)
	return (pSetLength, pSet)

def distinctPowers(LOWER_BOUND, UPPER_BOUND):
	aSeries = range(LOWER_BOUND, UPPER_BOUND+1)
	bSeries = range(LOWER_BOUND, UPPER_BOUND+1)
	pSeries = [[None for i in range(LOWER_BOUND, UPPER_BOUND+1)] for i in range(LOWER_BOUND, UPPER_BOUND+1)]
	for i,a in enumerate(aSeries):
		for j,b in enumerate(bSeries):
			if j == 0:
				pSeries[i][j] = a ** b
			else:
				pSeries[i][j] = pSeries[i][j-1] * a
	pSeries = matrix2list(pSeries)
	pSet = sorted(set(pSeries))
	pSetLength = len(pSet)
	return (pSetLength, pSet)

def solution():
	powers = distinctPowers(2, 100)
	print(powers)

solution()
