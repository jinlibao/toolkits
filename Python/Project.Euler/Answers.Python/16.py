# problem 16
# Project Euler

__author__ = 'Libao Jin'
__date__ = 'July 13, 2015'

def PowerDigitSum(powerOrder):
	power = 2 ** powerOrder
	strPower = str(power)
	intPower = []
	for i in strPower:
		intPower.append(int(i))
	# pds: PowerDigitSum
	pds = sum(intPower)
	return [pds, power, intPower]

def test():
	powerOrder = 1000
	pds = PowerDigitSum(powerOrder)
	print(pds)

test()
