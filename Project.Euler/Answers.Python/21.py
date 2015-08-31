# problem 
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

def properDivisors(primeFactors):
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

def amicabilize(number):
	primeFactors = primeFactor(number)
	if len(primeFactors) == 1:
		properDivisor = properDivisors(primeFactors)
	else:
		properDivisor = properDivisors(primeFactors)[0:-1]
	sumProperDivisor = sum(properDivisor)
	#print((number, primeFactors, properDivisor, sumProperDivisor))
	return sumProperDivisor

def solution(UpperBound):
	numbers = range(1, UpperBound+1)
	pairedNumbers = []
	ePairedNumbers = []
	for i in numbers:
		ePairedNumbers.append((i, amicabilize(i)))
	for i in ePairedNumbers:
		if isAmicable(i):
			pairedNumbers.append(i)
		else:
			continue
	numbers = []
	for i in pairedNumbers:
		if i[0] != i[1]:
			numbers.append(i[0])
			numbers.append(i[1])
	amicableNumbers = sorted(set(numbers))
	sumAmicableNumbers = sum(amicableNumbers)
	return (sumAmicableNumbers, amicableNumbers, pairedNumbers)
	
def isAmicable(thePairedNumber):
	number1, number2 = thePairedNumber
	if amicabilize(number2) == number1:
		return True
	else:
		return False

def test():
	#lists = binaryTree(6)
	#print(lists)
	#primeFactors = primeFactor(76576500)
	#factors = properDivisors(primeFactors)
	#print(factors)
	pairedNumber = solution(10000)
	print(pairedNumber)

test()
