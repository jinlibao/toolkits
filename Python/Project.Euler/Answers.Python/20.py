# problem 20
# Project Euler

__author__ = 'Libao Jin'
__date__ = 'July 17, 2015'

def factorial(n):
	product = 1
	while n > 1:
		product *= n
		n -= 1
	return product

def number2digits(number):
	string = str(number)
	digits = []
	for s in string:
		digits.append(int(s))
	return digits

def solution():
	f = factorial(100)
	d = number2digits(f)
	s = sum(d)
	result = (s,d,f)
	print(result)

solution()
