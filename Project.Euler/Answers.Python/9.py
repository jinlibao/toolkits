# problem 9
# Project Euler

__author__ = 'Libao Jin'
__date__ = 'July 12, 2015'

def isPythagoreanTriplets(a,b,c):
	'''This method judges whether a, b, c is Pythagorean Triplets, 
	if yes, return True, otherwise return False.'''
	if a**2 + b**2 == c**2:
		return True
	else:
		return False

def PythagoreanTriplets(n):
	a = range(1,n)
	b = range(1,n)
	for i in a:
		for j in b:
			c = n - i - j
			if isPythagoreanTriplets(i,j,c):
				product = i * j * c 
				#print(i, j, c, product)
				return (i, j, c, product)

def rangePythagoreanTriplets(UpperBound):
	sequenceN = range(1,UpperBound)
	numbersAvailable = []
	for k in sequenceN:
		p = PythagoreanTriplets(k)
		if p is not None:
			t = [k, p]
			numbersAvailable.append(t)
	return numbersAvailable
	
def test():
	rpt = rangePythagoreanTriplets(500)
	for i in rpt:
		print(i)

def run():
	print(PythagoreanTriplets(1000)[-1])

print('''------------ test() --------------''')
test()
print('''------------ run() ---------------''')
run()
