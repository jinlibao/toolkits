# problem 19
# Project Euler

__author__ = 'Libao Jin'
__date__ = 'July 17, 2015'

def isLeapYear(year):
	if year % 400 == 0:
		return True
	elif year % 100 != 0 and year % 4 == 0:
		return True
	else:
		return False

def daysInYear(date):
	year, month, day = date
	months = range(1, month)
	days = 0

	for m in months:
		days += daysOfMonth(year, m)

	days += day
	return days

def daysInYearReversed(date):
	days = daysOfYear(date[0]) - daysInYear(date)
	return days

def daysOfYear(year):
	if isLeapYear(year):
		days = 366
	else:
		days = 365
	return days

def daysOfMonth(year, month):
	if month == 1\
		or month == 3\
		or month == 5\
		or month == 7\
		or month == 8\
		or month == 10\
		or month == 12:
			days = 31
	elif month == 2:
		if isLeapYear(year):
			days = 29
		else:
			days = 28
	else:
		days = 30
	return days

def countDays(dateStart, dateEnd):
	yearStart, monthStart, dayStart = dateStart
	yearEnd, monthEnd, dayEnd = dateEnd
	years = range(yearStart+1, yearEnd)
	days = daysInYearReversed(dateStart)
	days += daysInYear(dateEnd)
	for y in years:
		days += daysOfYear(y)
	return days

def whichDay(date):
	dateFrom = (1900, 1, 1)
	days = countDays(dateFrom, date)
	remainder = days % 7 
	
	if remainder == 0:
		day = 'Monday'
	elif remainder == 1:
		day = 'Tuesday'
	elif remainder == 2:
		day = 'Wednesday'
	elif remainder == 3:
		day = 'Thursday'
	elif remainder == 4:
		day = 'Friday'
	elif remainder == 5:
		day = 'Saturday'
	elif remainder == 6:
		day = 'Sunday'

	return day

def directMethod():
	dateStart = (1901, 1, 1)
	dateEnd = (2000, 12, 31)
	years = range(dateStart[0], dateEnd[0]+1)
	months = range(1, 13)
	Sundays = []
	for y in years:
		for m in months:
			firstOfMonth = (y, m, 1)
			if whichDay(firstOfMonth) == 'Sunday':
				Sundays.append(firstOfMonth)
	return (len(Sundays), Sundays)

def test():
	#dateStart = (1993, 7, 17)
	#dateEnd = (2015, 7, 17)
	#days = countDays(dateStart, dateEnd)
	#print(days)
	#day = whichDay(dateEnd)
	#print(day)

	result = directMethod()
	print(result)
test()
