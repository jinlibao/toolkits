# problem 24
# Project Euler

__author__ = 'Libao Jin'
__date__ = 'July 17, 2015'

def factorial(n):
	product = 1
	while n > 1:
		product *= n
		n -= 1
	return product

def genStringNumbers(n):
	numbers = list(range(0,n))
	seq = []
	snumbers = []
	for i in numbers:
		snumbers.append(str(i))
	return snumbers

def genFSeries(n):
	fseries = []
	for i in range(1,n+1):
		fseries.append(factorial(i))
	return fseries

def lPermutation(pos, snumbers, fseries):
	if len(snumbers) <= 3:
		seq = []
		index = None
		index = len(snumbers) - 1
		quotient = pos // fseries[index-1]
		remainder = pos % fseries[index-1]
		#print(index, quotient, remainder, snumbers)
		p = snumbers.pop(quotient)
		seq.append(p)
		p = snumbers.pop(remainder)
		seq.append(p)
		seq += snumbers

		return seq
	else:
		seq = []
		index = len(snumbers)-1
		quotient = pos // fseries[index-1]
		remainder = pos % fseries[index-1]
		#print(index, pos, quotient, remainder, fseries[index])
		pos = remainder
		p = snumbers.pop(quotient)
		seq.append(p)
		seq += lPermutation(pos, snumbers, fseries)
		
		return seq

def string2number(strings):
	string = ''
	for s in strings:
		string += s
	integer = int(string)
	return integer
	
def solution():
	fseries = genFSeries(10)
	snumbers = genStringNumbers(10)
	seq = lPermutation(1000000, snumbers, fseries)
	intSeq = string2number(seq)
	print(intSeq)

def test():
	fseries = genFSeries(3)
	snumbers = genStringNumbers(3)
	indice = range(0,6)
	for i in indice:
		snumbers2 = snumbers.copy()
		seq = lPermutation(i, snumbers2, fseries)

solution()
#test()

