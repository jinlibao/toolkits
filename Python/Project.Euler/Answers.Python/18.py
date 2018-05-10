# problem 18
# Project Euler

__author__ = 'Libao Jin'
__date__ = 'July 17, 2015'

string = '''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''

def string2triangle(string):
	string = string[1:-1]
	string = string.split('\n')
	triangle = []
	for s in string:
		substrings = s.split(' ')
		integers = []
		for ss in substrings:
			integers.append(int(ss))
		triangle.append(integers)
	return triangle

def size(triangle):
	numberOfRows = len(triangle)
	numberOfColsMax = len(triangle[-1])
	return (numberOfRows, numberOfColsMax)

def accumulateSum(numberList):
	newNumberList = []
	for i,e in enumerate(numberList):
		newNumberList.append(sum(numberList[0:i]))
	return newNumberList

def recursiveGen(n):
	directions = [0,1]
	if n == 1:
		return [[0]]
	#if n == 2:
		#routes = []
		#newRoutes = []
		#for i in range(len(directions)):
			#route = routes.copy()
			#newRoutes.append(route)
		#for i,e in enumerate(newRoutes):
			#e.append(directions[i])
		#return newRoutes
	else:
		routes = recursiveGen(n-1)
		newRoutes = []
		for i in routes:
			for j in directions:
				route = i.copy()
				route.append(j)
				newRoutes.append(route)
		return newRoutes

def bruteForce(triangle):
	sizeTriangle = size(triangle)
	routes = recursiveGen(sizeTriangle[0])
	for i,e in enumerate(routes):
		routes[i] = accumulateSum(e)
	Sum = []
	maxIndex = -1
	for i in routes:
		tmp = 0
		for j in range(sizeTriangle[0]):
			tmp += triangle[j][i[j]]
		Sum.append(tmp)
	maxSum = max(Sum)
	for i,e in enumerate(Sum):
		if e == maxSum:
			maxIndex = i
	bestRoute = routes[maxIndex]
	bestNumbers = []
	for i in range(sizeTriangle[0]):
		bestNumbers.append(triangle[i][bestRoute[i]])
	return (maxSum, bestRoute, bestNumbers)
		
def solution():
	triangle = string2triangle(string)	
	print(bruteForce(triangle))
			
def test():
	triangle = string2triangle(string)	
	print(triangle)
	sizeTriangle = size(triangle)
	print(sizeTriangle)
	allRoutes = recursiveGen(7)
	print(allRoutes)

solution()
