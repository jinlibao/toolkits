# problem 15
# Project Euler

__author__ = 'Libao Jin'
__date__ = 'July 13, 2015'

def LatticePaths(numberOfGrids):
	numberOfPaths = nchoosek(2*numberOfGrids, numberOfGrids)
	return numberOfPaths
	
def factorial(n):
	fact = 1
	i = 1
	while i <= n:
		fact *= i
		i += 1
	return fact

def nchoosek(n, k):
	nck = factorial(n) // (factorial(k) * factorial(n-k))
	return nck

## Wrong idea
#def accumulateSum(n):
	#s = 0
	#i = 1
	#while i <= n:
		#s += i
		#i += 1
	#return s

#def LatticePaths_method2(numberOfGrids):
	#numberOfPaths = 2 * accumulateSum(numberOfGrids+1)
	#return numberOfPaths

def test():
	lp = LatticePaths(3)
	print(lp)
	lp2 = LatticePaths(20)
	print(lp2)
	#lp3 = LatticePaths_method2(3)
	#print(lp3)
	#lp4 = LatticePaths_method2(20)
	#print(lp4)

test()
