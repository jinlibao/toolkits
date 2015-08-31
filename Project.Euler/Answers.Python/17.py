# problem 17
# Project Euler

__author__ = 'Libao Jin'
__date__ = 'July 14, 2015'

def oneDigitTransform(number):
	if number == 1:
		numberInString = 'one'
	elif number == 2:
		numberInString = 'two'
	elif number == 3:
		numberInString = 'three'
	elif number == 4:
		numberInString = 'four'
	elif number == 5:
		numberInString = 'five'
	elif number == 6:
		numberInString = 'six'
	elif number == 7:
		numberInString = 'seven'
	elif number == 8:
		numberInString = 'eight'
	elif number == 9:
		numberInString = 'nine'
	elif number == 0:
		numberInString = 'zero'
	else:
		numberInString = ''
	return numberInString

def twoDigitsTransform(number):
	decimal = number // 10
	unit = number % 10
	numberInString = ''

	if decimal == 1:
		if number == 10:
			numberInString = 'ten'
		elif number == 11:
			numberInString = 'eleven'
		elif number == 12:
			numberInString = 'twelve'
		elif number == 13:
			numberInString = 'thirteen'
		elif number == 14:
			numberInString = 'fourteen'
		elif number == 15:
			numberInString = 'fifteen'
		elif number == 16:
			numberInString = 'sixteen'
		elif number == 17:
			numberInString = 'seventeen'
		elif number == 18:
			numberInString = 'eighteen'
		elif number == 19:
			numberInString = 'nineteen'
		return numberInString
	elif decimal == 2:
		numberInString += 'twenty'
	elif decimal == 3:
		numberInString += 'thirty'
	elif decimal == 4:
		numberInString += 'forty'
	elif decimal == 5:
		numberInString += 'fifty'
	elif decimal == 6:
		numberInString += 'sixty'
	elif decimal == 7:
		numberInString += 'seventy'
	elif decimal == 8:
		numberInString += 'eighty'
	elif decimal == 9:
		numberInString += 'ninety'
	else:
		numberInString += ''

	if unit != 0:
		if decimal != 0:
			numberInString += '-' + oneDigitTransform(unit)
		else:
			numberInString += oneDigitTransform(unit)

	return numberInString

def threeDigitsTransform(number):
	numberInString = ''
	hundred = number // 100
	remain = number % 100
	
	if hundred != 0:
		numberInString += oneDigitTransform(hundred) + ' hundred'

	if remain != 0:
		if hundred != 0:
			numberInString += ' and ' + twoDigitsTransform(remain)
		else:
			numberInString += twoDigitsTransform(remain)
	
	return numberInString

def fourDigitsTransform(number):
	numberInString = ''
	thousand = number // 1000
	remain = number % 1000
	
	if thousand != 0:
		numberInString += threeDigitsTransform(thousand) + ' thousand'

	if remain != 0:
		if thousand != 0:
			numberInString += ' and ' + threeDigitsTransform(remain)
		else:
			numberInString += threeDigitsTransform(remain)
	
	return numberInString

def recursiveTransform(number):
	numberInString = ''
	numberDigits = howManyDigits(number)
	if numberDigits <= 6:
		numberInString += fourDigitsTransform(number)
		return numberInString
	elif numberDigits > 6 and numberDigits <= 9:
		numberOut = number // 1000000
		number = number % 1000000
		numberInString += fourDigitsTransform(numberOut) + ' million and '
		numberInString += recursiveTransform(number)
	elif numberDigits > 9 and numberDigits <= 12:
		numberOut = number // 1000000000
		number = number % 1000000000
		numberInString += fourDigitsTransform(numberOut) + ' billion and '
		numberInString += recursiveTransform(number)
	elif numberDigits > 12 and numberDigits <= 15:
		numberOut = number // 1000000000000
		number = number % 1000000000000
		numberInString += fourDigitsTransform(numberOut) + ' trillion and '
		numberInString += recursiveTransform(number)
	return numberInString

def howManyDigits(number):
	numberOfDigits = len(str(number))
	return numberOfDigits

def computeNumberOfLetters(numberInString):
	numberInString = numberInString.replace(' ','')
	numberInString = numberInString.replace('-','')
	#print(numberInString, len(numberInString))
	return len(numberInString)



def test():

	problem17 = 'problem17result2.txt'
	f = open(problem17, 'w+', encoding = 'utf-8')

	#seq1 = range(0,10)
	#print('-------------------- oneDigitTransform --------------------')
	#for i in seq1:
		#print(i, '->', oneDigitTransform(i))
	#seq2 = range(10,100)
	#print('-------------------- twoDigitsTransform --------------------')
	#for j in seq2:
		#print(j, '->', twoDigitsTransform(j))
	#seq3 = range(100,122)
	#print('-------------------- threeDigitsTransform --------------------')
	#for k in seq3:
		#print(k, '->', threeDigitsTransform(k))
	seq4 = range(0,90)
	computeNumberOfLetters(recursiveTransform(342))
	computeNumberOfLetters(recursiveTransform(115))
	print('-------------------- numberToWords --------------------')
	for n in seq4:
		result = str(n) + ' -> ' + recursiveTransform(n)
		#print(n, '->', numberToWords(n))
		#print(result)
		f.write(result)
		f.write('\n')
	f.close()

def solution():
	problem17 = 'problem17result2.txt'
	f = open(problem17, 'w+', encoding = 'utf-8')

	seq = range(1,1001)
	length = []
	for i in seq:
		l = computeNumberOfLetters(recursiveTransform(i))
		length.append(l)

		result = str(i) + ' -> ' + recursiveTransform(i)
		f.write(result)
		f.write('\n')

	print('from 1 to 1000:', sum(length), length)
	f.close()

solution()
