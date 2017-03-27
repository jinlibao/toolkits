# problem 58
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

def list2stringList(list):
	stringList = []
	for l in list:
		for s in l:
			stringList.append(s)
	return stringList

def direction(UPPER_BOUND):
	orientation = ['R', 'D', 'L', 'U']
	rSeq = list(range(1, UPPER_BOUND+2, 2))
	dSeq = list(range(1, UPPER_BOUND+2, 2))
	lSeq = list(range(2, UPPER_BOUND+2, 2))
	uSeq = list(range(2, UPPER_BOUND+2, 2))
	#print(rSeq, dSeq, lSeq, uSeq)
	i = 0
	directions = [rSeq[i]*orientation[0]]
	index = rSeq[i]

	while index < UPPER_BOUND ** 2:
		directions.append(dSeq[i] * orientation[1])
		directions.append(lSeq[i] * orientation[2])
		directions.append(uSeq[i] * orientation[3])
		directions.append(rSeq[i+1] * orientation[0])
		index += dSeq[i] + lSeq[i] + uSeq[i] + rSeq[i+1]
		i += 1
	directions = list2stringList(directions)
	#print(directions)
	return directions

def route(UPPER_BOUND):
	directions = direction(UPPER_BOUND)
	point = (UPPER_BOUND+1) // 2
	currentPoint = (point-1, point-1)
	pointInfo = []
	pointInfo.append((1, currentPoint))

	for i,e in enumerate(directions[0:-1]):
		if e == 'R':
			currentPoint = (currentPoint[0], currentPoint[1] + 1)
			pointInfo.append((i+2, currentPoint))
		elif e == 'D':
			currentPoint = (currentPoint[0] + 1, currentPoint[1])
			pointInfo.append((i+2, currentPoint))
		elif e == 'L':
			currentPoint = (currentPoint[0], currentPoint[1] - 1)
			pointInfo.append((i+2, currentPoint))
		elif e == 'U':
			currentPoint = (currentPoint[0] - 1, currentPoint[1])
			pointInfo.append((i+2, currentPoint))
	return pointInfo

def matrix(UPPER_BOUND):
	matrix = [[None for i in range(UPPER_BOUND)] for i in range(UPPER_BOUND)]
	pointInfo = route(UPPER_BOUND)
	for p in pointInfo:
		matrix[p[1][0]][p[1][1]] = p[0]

	#for i in matrix:
		#print(i)
	return matrix

def size(matrix):
	rowLength = len(matrix)
	colLength = len(matrix[0])
	sizeOfMatrix = (rowLength, colLength)
	return sizeOfMatrix

def extractDiagonalNumbers(matrix):
	sizeOfMatrix = size(matrix)
	index = range(sizeOfMatrix[0])
	dNumbers = []
	for i in index:
		dNumbers.append(matrix[i][i])
	for i in index:
		dNumbers.append(matrix[i][-(i+1)])
	dNumbers = sorted(set(dNumbers))
	return dNumbers

def computeRatioOfPrimes(numbers):
	primes = []
	for i in numbers:
		if isPrime(i):
			primes.append(i)
	numberOfPrimes = len(primes)
	numberOfNumbers = len(numbers)
	ratioOfPrimes = numberOfPrimes / numberOfNumbers
	return (ratioOfPrimes, (numberOfPrimes, numberOfNumbers), primes)

def spiralPrimes(UPPER_BOUND):
	ratioOfPrimes = 1
	while ratioOfPrimes > 0.1:
		UPPER_BOUND += 1
		m = matrix(UPPER_BOUND)
		dn = extractDiagonalNumbers(m)
		ratioOfPrimesInfo = computeRatioOfPrimes(dn)
		ratioOfPrimes = ratioOfPrimesInfo[0]
		#print(UPPER_BOUND, ratioOfPrimes)
	return (UPPER_BOUND, ratioOfPrimesInfo)

def solution():
	UPPER_BOUND = 690
	ratioOfPrimes = spiralPrimes(UPPER_BOUND)
	print(ratioOfPrimes)

solution()
