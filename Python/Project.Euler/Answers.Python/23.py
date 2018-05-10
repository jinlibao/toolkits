# problem 23
# Project Euler

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

def properDivisor(primeFactors):
	n = len(primeFactors) # n: numberOfPFactors
	properDivisors = [None for i in range(2 ** n)]
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
		properDivisors[index] = factor
	properDivisors = sorted(set(properDivisors))
	return properDivisors

def primeFactor(number):
	primeFactors = [1]
	bound = number // 2
	i = 2
	while i <= bound:
		if number % i == 0:
			primeFactors.append(i)
			number //= i
		else:
			i += 1
	if len(primeFactors) == 1:
		primeFactors.append(number)

	return primeFactors

def isAbundant(number):
	primeFactors = primeFactor(number)
	properDivisors = properDivisor(primeFactors)[0:-1]
	sumProperDivisors = sum(properDivisors)
	if sumProperDivisors > number:
		return True
	else:
		return False

def abundantNumber():
	numbers = range(1, 28123)
	abundantNumbers = []
	for i in numbers:
		if isAbundant(i):
			abundantNumbers.append(i)
	return abundantNumbers

def isSumOfAbundantNumber(abundantNumbers, number):
	for i in abundantNumbers:
		if number - i > 0 and abundantNumbers.__contains__(number - i):
			return True
		elif number - i < 0:
			return False
		else:
			continue
#def isSumOfAbundantNumber(abundantNumbers, number):
	#if abundantNumbers.__contains__(number) and number >= 48 :
		#return True
	#else:
		#for i in abundantNumbers:
			#if number-i > 0 and abundantNumbers.__contains__(number-i):
				#return True
			#elif number-i < 0:
				#return False
			#else:
				#continue

def nonAbundantNumber():
	abundantNumbers = abundantNumber()
	#print('abundantNumbers:')
	#print(abundantNumbers)
	orderedNumbers = list(range(1, 24))
	oddNumbers = []
	for i in range(1,14062):
		oddNumbers.append(2*i+1)
	nonAbundantNumbers = orderedNumbers + oddNumbers
	#print('candidateNumbers:')
	for i in range(13,14062):
		candidateNumber = 2*i
		if not isSumOfAbundantNumber(abundantNumbers, candidateNumber):
			nonAbundantNumbers.append(candidateNumber)

	return list(set(nonAbundantNumbers))

def solution():
	nonAbundantNumbers = nonAbundantNumber()
	#print('results\n')
	print(sum(nonAbundantNumbers), nonAbundantNumbers)

solution()
