'''
tdc.py
get teacher's data
'''

import urllib.request
import urllib.parse
import re
import threading
import time

def get_headers():
	accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
	accept_language = 'en-US,en;q=0.5'
	#cache_control = 'no-cache'
	connection = 'Keep-Alive'
	#content_length = '64'
	#content_type = 'application/x-www-form-urlencoded'
	cookie = 'JSESSIONID=FDC43A684C6B273063EA54351A8CF8E3'
	host = 'www.tdc.zjut.edu.cn'
	referer = 'http://www.tdc.zjut.edu.cn/UTADB/search_normal?table=0&field2=deptclass_one&condition2='
	user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'
	headers = {}
	headers['Accept'] = accept
	headers['Accept-Language'] = accept_language
	#headers['Cache-Control'] = cache_control
	headers['Connection'] = connection
	#headers['Content-Length'] = content_length
	#headers['Content-Type'] = content_type
	headers['Cookie'] = cookie
	headers['Host'] = host
	headers['Referer'] = referer
	headers['User-Agent'] = user_agent
	return headers

def save_page(the_page, filename='the_page.html'):
	f = open(filename, 'w+')
	f.write(the_page)
	f.close()

def get_data(campus, page):
	values = {}
	values['table'] = ''
	values['field2'] = 'deptclass_one'
	values['condition2'] = campus
	values['page'] = page
	#values['ok2'] = u'查 询'.encode('gbk')
	data = urllib.parse.urlencode(values)
	data = data.encode('utf-8')
	return data

def save_page(the_page, filename='tdc.html'):
	f = open(filename, 'w+')
	f.write(the_page)
	f.close()

def get_info(Campus, page):
	prefix, campus, upper_bound = Campus
	
	url = 'http://www.tdc.zjut.edu.cn/UTADB/search_normal'
	headers = get_headers()
	data = get_data(campus, page)
	if page <= upper_bound:
		req = urllib.request.Request(url, data=data, headers=headers)
		with urllib.request.urlopen(req) as response:
			the_page = response.read().decode('gbk')
			filename = './tdc/{0}_tdc_{1}.html'.format(prefix, str(page).zfill(2))
			save_page(the_page, filename)
			print('{0} saved.'.format(filename))

if __name__ == '__main__':
	campuses = []
	campuses.append(['pf', u'屏峰校区'.encode('gbk'), 64])
	campuses.append(['zh', u'朝晖校区'.encode('gbk'), 91])
	campuses.append(['zj', u'之江校区'.encode('gbk'), 23])

	s_time = time.time()
	pages = range(91, 92)
	for Campus in campuses:
		for page in pages:
			get_info(Campus, page)
	e_time = time.time()
	elapsed_time = e_time - s_time
	print('Time elapsed: {0:.2f} seconds.'.format(elapsed_time))
