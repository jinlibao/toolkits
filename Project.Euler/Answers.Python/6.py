# Problem 6
# https://projecteuler.net/problem=6
# 
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# 
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# 
# Hence the difference between the sum of the squares of the first ten
# natural numbers and the square of the sum is 3025 - 385 = 2640.
# 
# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.
# 
# Libao Jin
# March 15, 2015

def SumSquareDifference(n):
	squares = [x ** 2 for x in range(n+1)]
	numbers = [x for x in range(n+1)]
	difference = sum(numbers) ** 2 - sum(squares) 
	return difference

d = SumSquareDifference(100)
print d
