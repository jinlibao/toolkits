# problem 12
# Project Euler

import math

__author__ = 'Libao Jin'
__date__ = 'July 13, 2015'

def AccumulateSumSequence(n):
	seq = []
	i = 1
	currentValue = 0
	while i <= n:
		currentValue += i
		seq.append(currentValue)
		i += 1
	return seq

def AccumulateSumGenerator(n):
	number = 0
	i = 1
	while i <= n:
		number += i
		i += 1
	return number

def Factorization(n):
	currentFactor = 1
	factors = []

	while currentFactor <= n // 2:
		if n % currentFactor == 0:
			factors.append(currentFactor)
		currentFactor += 1
	
	factors.append(n)
	return factors

def SeqFactors(n):
	seq = AccumulateSumSequence(n)
	numfactors = []

	for i in seq:
		factors = Factorization(i)
		numfactors.append([i,len(factors),factors])
	
	return numfactors

def NumberFactors(LengthBound):
	length = 0
	n = 1
	while length <= LengthBound:
		number = AccumulateSumGenerator(n)
		factors = Factorization(number)
		length = len(factors)
		n += 1
	numberInfo = [number, len(factors), factors]
	return numberInfo

def test1():
	s = SeqFactors(10)
	for i in s:
		print(i)

def solution():
	result = NumberFactors(500)
	print(result)

#test1()
solution()
