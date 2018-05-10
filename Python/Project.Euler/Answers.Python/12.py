# problem 12
# Project Euler

import math

__author__ = 'Libao Jin'
__date__ = 'July 17, 2015'

def binaryTree(n):
	directions = [0, 1]
	if n == 1:
		return [[0], [1]]
	else:
		sonTree = binaryTree(n-1)
		newTree = []
		for s in sonTree:
			for d in directions:
				ssTree = s.copy()
				ssTree.append(d)
				newTree.append(ssTree)

		return newTree

def allFactor(primeFactors):
	n = len(primeFactors) # n: numberOfPFactors
	Factors = [None for i in range(2 ** n)]
	factorsTree = binaryTree(n)
	for ft in factorsTree:
		index = 0
		for i,e in enumerate(ft):
			index += e * (2 ** (n-i-1))
		#print(index)
		factor = 1
		for i,e in enumerate(ft):
			if e == 1:
				factor *= primeFactors[i]
		Factors[index] = factor
	Factors = sorted(set(Factors))
	return Factors

def primeFactor(number):
	primeFactors = [1]
	bound = math.sqrt(number)
	i = 2
	while i <= bound:
		if number % i == 0:
			primeFactors.append(i)
			number //= i
		else:
			i += 1
	return primeFactors

def triangularNumber(n):
	seq = []
	i = 1
	tNumber = 0
	while i <= n:
		tNumber += i
		i += 1
	return tNumber

def HDTN(BOUND):
	i = 1
	tNumber = triangularNumber(i)	
	primeFactors = primeFactor(tNumber)
	Factors = allFactor(primeFactors)
	lengthFactor = len(Factors)
	while lengthFactor < BOUND:
		i += 1
		tNumber = triangularNumber(i)	
		primeFactors = primeFactor(tNumber)
		Factors = allFactor(primeFactors)
		lengthFactor = len(Factors)
	numberInfo = (tNumber, lengthFactor, Factors)
	return numberInfo

def solution():
	numberInfo = HDTN(500)
	print(numberInfo)

solution()
