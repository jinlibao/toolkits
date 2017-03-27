# problem 53
# Project Euler

__author__ = 'Libao Jin'
__date__ = 'July 17, 2015'


def factorial(n):
	if n <= 1:
		return 1
	product = 1
	while n > 1:
		product *= n
		n -= 1
	return product

def factorialSeries(n):
	fSeries = []
	for i in range(n):
		if i == 0:
			fSeries.append(1)
		else:
			value = fSeries[i-1] * i
			fSeries.append(value)
	return fSeries

def NChooseR(N, R):
	#nchooser = fSeries[N] / (fSeries[R] * fSeries[N-R])
	nchooser = factorial(N) // (factorial(R) * factorial(N-R))
	return nchooser

def combinatoricSelection(start, end, BOUND):
	n = range(start, end+1)
	selectedSeries = []
	for i in n:
		r = range(i)
		for j in r:
			nchooser = NChooseR(i, j)
			if nchooser > BOUND:
				selectedSeries.append((i, j, nchooser))
	return (len(selectedSeries), selectedSeries)

def solution():
	selectedSeriesInfo = combinatoricSelection(1, 100, 1000000)
	for i,e in enumerate(selectedSeriesInfo):
		if i == 0:
			print(e)
		else:
			for j in e:
				print(j)
	#print(selectedSeriesInfo)

solution()
