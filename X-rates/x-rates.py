# -*- coding: utf-8 -*-
'''
x-rate
'''

__author__ = 'Libao Jin'
__date__ = 'Aug 31, 2015'

import urllib.parse
import urllib.request
import re
import csv
import time
import os
import threading

def format_date(date):
	year, month, day = date
	date = str(year).zfill(2) + '-' + str(month).zfill(2) + '-' + str(day).zfill(2)
	return date

def is_leap_year(year):
	if year % 400 == 0:
		return True
	elif year % 100 != 0 and year % 4 == 0:
		return True
	else:
		return False

def days_in_year(date):
	year, month, day = date
	months = range(1, month)
	days = 0

	for m in months:
		days += days_of_month(year, m)

	days += day
	return days

def days_in_year_reversed(date):
	days = days_of_year(date[0]) - days_in_year(date)
	return days

def days_of_year(year):
	if is_leap_year(year):
		days = 366
	else:
		days = 365
	return days

def days_of_month(year, month):
	if month in [1, 3, 5, 7, 8, 10, 12]:
		days = 31
	elif month in [4, 6, 9, 11]:
		days = 30
	else:
		if is_leap_year(year):
			days = 29
		else:
			days = 28
	return days

def make_date_range(s_date, e_date):
	s_year, s_month, s_day = s_date
	e_year, e_month, e_day = e_date
	years = range(s_year, e_year + 1)
	days = 0

	if len(years) == 1:
		days = days_in_year(e_date) - days_in_year(s_date)
	elif len(years) > 1:
		for y in years:
			if y == s_year:
				days += days_in_year_reversed(s_date)
			elif y == e_year:
				days += days_in_year(e_date)
			else:
				days += days_of_year(y)

	dates = []
	dates.append(format_date(s_date))

	while days > 0:
		days_bound = days_of_month(s_year, s_month)
		if s_day + 1 <= days_bound:
			s_day += 1
		elif s_day + 1 > days_bound:
			s_day = 1
			if s_month + 1 <= 12:
				s_month += 1
			else:
				s_month = 1
				s_year += 1
		s_date = (s_year, s_month, s_day)
		dates.append(format_date(s_date))
		days -= 1
	return dates


def get_xrates():
	'visit x-rates site and grab the exchange rate'
	url = 'http://www.x-rates.com/table/'
	values = {'from': 'CNY', 'amount':'1'}
	user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'
	headers = { 'User-Agent' : user_agent}
	data = urllib.parse.urlencode(values)
	data = data.encode('utf-8') # data should be bytes
	req = urllib.request.Request(url, data, headers)
	with urllib.request.urlopen(req) as response:
		the_page = response.read().decode('utf-8')
		return the_page

def get_xrates_by_date(search_date):
	'visit x-rates site and grab the exchange rate'
	except_time = 0
	url = 'http://www.x-rates.com/historical/?date={0}&amount=1&from=CNY'.format(search_date)
	req = urllib.request.Request(url)
	try:
		with urllib.request.urlopen(req) as response:
			the_page = response.read().decode('utf-8')
			return the_page
	except urllib.error.URLError:
		except_time += 1
		if except_time < 2:
			print('Error! Try to access {} again.'.format(search_date))
			the_page = get_xrates_by_date(search_date)
			return the_page
		else:
			print('Error! Pass {}.'.format(search_date))
			return None

def get_xrates_by_date2(search_date):
	'visit x-rates site and grab the exchange rate'
	url = 'http://www.x-rates.com/historical/'
	values = {'date': search_date, 'amount': '1','from': 'CNY'}
	user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'
	headers = { 'User-Agent' : user_agent}
	data = urllib.parse.urlencode(values)
	data = data.encode("utf-8") # data should be bytes
	req = urllib.request.Request(url, data, headers)
	with urllib.request.urlopen(req) as response:
		the_page = response.read().decode('utf-8')
		return the_page


def save_page(local_file, the_page):
	'save the page into local files'
	f = open(local_file, 'w+', encoding = 'utf-8')
	f.write(the_page)
	f.close()

def combine_data(folder):
	os.chdir(folder)
	files = os.listdir('.')
	ext_filter = '.*\.csv'
	p = re.compile(ext_filter)
	csv_files = []
	for f in files:
		m = p.match(f)
		if m:
			csv_files.append(m.group())
		else:
			continue
	print(csv_files)
	header = ['Time']
	total_data = r'..\x-rates_all.csv'
	td = open(total_data, 'w+', encoding = 'utf-8')
	for i, cf in enumerate(csv_files):
		data = {}
		with open(cf, 'r', encoding = 'utf-8') as f:
			csv_reader = csv.DictReader(f)
			for row in csv_reader:
				if i < 1:
					header.append(row['Country'])
				data['Time'] = row['Time']
				data[row['Country']] = row['To']
		if i < 1:
			csv_writer = csv.DictWriter(td, fieldnames = header)
			csv_writer.writeheader()
		csv_writer.writerow(data)
		print(i, cf)

	td.close()
	os.chdir('..')

def parse_data(the_page, current_time, folder):

	pattern = '^\t*<td.*?>(<a.*?>)?(.*?)<\/.*>'
	p = re.compile(pattern, re.M)
	m = p.findall(the_page)
	data = []

	if m is not None:
		for i,e in enumerate(m):
			#print(i, e[1])
			if i < 30:
				continue
			if i % 3 == 0:
				sub_data = {}
				sub_data['Time'] = current_time
				sub_data['Country'] = e[1]
				#sub_data = []
				#sub_data.append(e[1])
			elif i % 3 == 1:
				sub_data['From'] = e[1]
			elif i % 3 == 2:
				sub_data['To'] = e[1]
				data.append(sub_data)


	outputfile= folder + r'\x-rates_' + current_time + '.csv'
	csvfileout = open(outputfile, 'w+')
	headers = ['Country', 'From', 'To', 'Time']
	cw = csv.DictWriter(csvfileout, fieldnames = headers)
	cw.writeheader()

	for d in data:
		if d['Country'] == 'US Dollar':
			print(current_time, d['Country'], d['To'])
		cw.writerow(d)

	csvfileout.close()
	return data

def do_task(current_time, folder):
	the_page = get_xrates()
	#local_file = 'x-rates.html'
	#save_page(local_file, the_page)
	parse_data(the_page, current_time, folder)

def do_task_by_date(s_date = (2005, 2, 4), e_date = (2015, 8, 30)):

	folder = 'daily'
	dates = make_date_range(s_date, e_date)
	for date in dates:
		the_page = get_xrates_by_date(date)
		parse_data(the_page, date, folder)
		#time.sleep(1)

def do_task_repeatedly(period=60):
	folder = 'data'
	while True:
		ct = time.gmtime()
		current_time = convert_time(ct)
		do_task(current_time, folder)
		time.sleep(period)

def convert_time(ct):
	s = str(ct.tm_year).zfill(2) + '-' + str(ct.tm_mon).zfill(2) + '-' + str(ct.tm_mday).zfill(2) + '_' + str(ct.tm_hour).zfill(2) + '-' + str(ct.tm_min).zfill(2) + '-' + str(ct.tm_sec).zfill(2)
	return s

def clean_folder():
	files = os.listdir()
	print(files)
	pattern = '[-.a-zA-Z0-9]*~'
	p = re.compile(pattern)
	to_delete = []
	print('Files have been removed:')
	for f in files:
		m = p.match(f)
		if m:
			trash_file = m.group()
			print(trash_file)
			to_delete.append(trash_file)
			os.remove(trash_file)
		else:
			continue
def thread1():
	#t1 = threading.Thread(target = do_task_by_date, args = ((2005, 1, 1), (2005, 12, 31)))
	t1 = threading.Thread(target = check_files, args = ((2005, 1, 1), (2005, 12, 31)))
	t2 = threading.Thread(target = check_files, args = ((2006, 1, 1), (2006, 12, 31)))
	t3 = threading.Thread(target = check_files, args = ((2007, 1, 1), (2007, 12, 31)))
	t4 = threading.Thread(target = check_files, args = ((2008, 1, 1), (2008, 12, 31)))
	t4 = threading.Thread(target = check_files, args = ((2009, 1, 1), (2009, 12, 31)))
	t5 = threading.Thread(target = check_files, args = ((2010, 1, 1), (2010, 12, 31)))
	t6 = threading.Thread(target = check_files, args = ((2011, 1, 1), (2011, 12, 31)))
	t7 = threading.Thread(target = check_files, args = ((2012, 1, 1), (2012, 12, 31)))
	t8 = threading.Thread(target = check_files, args = ((2013, 1, 1), (2013, 12, 31)))
	t9 = threading.Thread(target = check_files, args = ((2014, 1, 1), (2014, 12, 31)))
	t1.start()
	print('Thread-1 started.')
	t2.start()
	print('Thread-2 started.')
	t3.start()
	print('Thread-3 started.')
	t4.start()
	print('Thread-4 started.')
	t5.start()
	print('Thread-5 started.')
	t6.start()
	print('Thread-6 started.')
	t7.start()
	print('Thread-7 started.')
	t8.start()
	print('Thread-8 started.')
	t9.start()
	print('Thread-9 started.')

def check_files(s_date, e_date):
	dates = make_date_range(s_date, e_date)

	folder = r'.\daily\3kb'
	files = os.listdir(folder)
	#print(files)

	not_exist_dates = []
	for d in dates:
		n = 'x-rates_' + d + '.csv'
		if n not in files:
			not_exist_dates.append(d)
			#print(d)
	print(len(not_exist_dates))
	
	folder = 'daily'
	for date in not_exist_dates:
		the_page = get_xrates_by_date(date)
		parse_data(the_page, date, folder)
		time.sleep(1)


if __name__ == '__main__':

	clean_folder()
	#thread1()
	#combine_data(r'.\daily\3kb')
	#do_task_repeatedly()
	
	# do_task_repeatedly()
