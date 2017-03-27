# Problem 4
# https://projecteuler.net/problem=4
# 
# A palindromic number reads the same both ways. The largest
# palindrome made from the product of two 2-digit numbers is 9009 = 91
# x 99.
# 
# Find the largest palindrome made from the product of two 3-digit
# numbers.
# 
# Libao Jin
# March 15, 2015

import math

def isPalindromic(number):
	numberLength = int(math.ceil(math.log10(number)))
	digits = []

	while number > 0:
		digits.append(number % 10)
		number /= 10

	i = 0
	while i <= numberLength / 2:
		if digits[i] != digits[numberLength-i-1]:
			break
		else:
			i += 1
			
	if i > numberLength / 2:
		return True
	else:
		return False
	
def Palindromic(n):

	f = [10 ** (n)-1, 10 ** (n)-1]
	p = []
	while f[0] >= 10 ** (n-1):
		while f[1] >= 10 ** (n-1):
			d = f[0] * f[1]
			type = isPalindromic(d)
			if type == True:
				p.append(d)
				# print f[0], f[1]
				f[1] -= 1
			else:
				f[1] -= 1
		f[0] -= 1
		f[1] = f[0]
	# print p
	return max(p)

t = Palindromic(3)
print t
	
