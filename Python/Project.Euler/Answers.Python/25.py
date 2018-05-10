# problem 25
# Project Euler

__author__ = 'Libao Jin'
__date__ = 'July 17, 2015'

def Fibonacci(n):
	fibonacci = None
	if n < 3:	
		fibonacci = 1
		return fibonacci
	else:
		fibonacci = Fibonacci(n-1) + Fibonacci(n-2)
		return fibonacci

def genFibonacciSeq(upperBound):
	fibonacciSeq = [1,1]
	length = 1
	i = 2
	while length < upperBound:
		fibonacci = fibonacciSeq[i-1]+fibonacciSeq[i-2]
		length = len(str(fibonacci))
		fibonacciSeq.append(fibonacci)
		i += 1
	return fibonacciSeq

def test():
	#index = range(1,100)
	#for i in index:
		#print(Fibonacci(i))
	seq = genFibonacciSeq(1000)
	index = len(seq)
	print((index, seq[index-1], seq))

test()
