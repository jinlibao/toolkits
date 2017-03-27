# problem 48
# Project Euler

__author__ = 'Libao Jin'
__date__ = 'July 18, 2015'

def lastTenDigits(number):
	string = str(number)
	lastTen = int(string[-10:])
	return lastTen

def amazingSum(n):
	s = 0
	while n >= 1:
		s += n ** n
		n -= 1
	return s

def selfPowers(n):
	s = amazingSum(n)
	l = lastTenDigits(s)
	return (l, s)

def solution():
	ls = selfPowers(1000)
	print(ls)

solution()
