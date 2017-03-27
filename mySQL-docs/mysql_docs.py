# -*- coding: utf-8 -*-
'''
mysql_docs.py
Download reference manuals from http://dev.mysql.com/doc/
'''

import urllib.request
import re
import os
import time

__author__ = 'Libao Jin'
__date__ = 'Sept 08, 2015'

def get_header():
	header = {}
	header['Referer'] = 'http://dev.mysql.com/doc/'
	header['Cookie'] = 's_nr=1441605722245; MySQL_S=qeodg17hi9rak1utppdf4ecp2et6bpfd; s_cc=true; s_sq=sunmysql%3D%2526pid%253Dmysql%25253Adoc%252520%252528site%252520section%252529%2526pidt%253D1%2526oid%253Dhttp%25253A//downloads.mysql.com/docs/refman-5.6-en.epub%2526ot%253DA; gpName=mysql%3Adev%3A/doc/; gpChannel=mysql%3Adoc; gpServer=dev.mysql.com'
	header['Host'] = 'downloads.mysql.com'
	header['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240'
	return header

def fetch_files(url, file_type, path='files'):
	if not os.path.exists(path):
		os.mkdir(path)
	pattern = r'[-A-Za-z0-9.]*{0}'.format(file_type)
	p = re.compile(pattern)
	m = p.search(url)
	if m:
		filename = path + '/' + m.group()
		try:
			print('Downloading {0}'.format(filename))
			f = urllib.request.urlretrieve(url, filename)
			print('{0} downloaded.'.format(filename))
		except urllib.error.URLError:
			print('Files ({0}) does not exist.'.format(filename))

def extract_url(thepage, file_type='pdf'):
	pattern = r'"(http://.*?{0})"'.format(file_type)
	p = re.compile(pattern)
	g = p.findall(thepage)
	if g:
		print(len(g), g)
	return g

def download_refman(sql_url):
	header = get_header()
	#request = urllib.request.Request(sql_url, data=None, headers=header)
	request = urllib.request.Request(sql_url)
	thepage = urllib.request.urlopen(request).read().decode('utf-8')
	file_types = ['pdf']
	for file_type in file_types:
		urls = extract_url(thepage, file_type)
		for url in urls:
			fetch_files(url, file_type)
			time.sleep(10)

if __name__ == '__main__':
	download_refman('http://dev.mysql.com/doc/')
