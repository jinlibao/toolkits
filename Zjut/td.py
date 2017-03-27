# -*- coding: utf-8 -*-
'''
td.py
teachers' data
'''
import re
import os
import time
import csv

def save_file(list_items, filename):
	with open(filename, 'w+', encoding = 'utf-8') as f:
		for i in list_items:
			#print(i[:-1])
			f.write(i[:-1])
			#f.write('\n')

def get_info():
	infos = []
	folder = './tdc/'
	files = os.listdir(folder)
	os.chdir(folder)
	for filename in files:
		with open(filename, 'r') as f:
			page = f.read()
			info = extract_block(page)
			#print(info)
			infos += info
	os.chdir('..')
	return infos

def extract_block(page):
	pattern = '<tr bgcolor.*?(<td.*?)</font></tr>'
	p = re.compile(pattern, re.DOTALL)
	m = p.findall(page)
	#print(len(m), type(m))
	return m

def extract_info(block):
	d = {}
	id_pattern = '<U>(\d*)'
	p = re.compile(id_pattern)
	id_m = p.search(block)
	if id_m:
		d['id'] = id_m.group(1)
	pattern = 'td.*?(>.*? *<)/td'
	p = re.compile(pattern)
	m = p.findall(block)
	
	try:
		d['name'] = m[2][1:-1].replace(' ','')
		d['campus'] = m[3][1:-1].replace(' ','')
		d['college'] = m[4][1:-1].replace(' ','')
		d['department'] = m[5][1:-1].replace(' ','')
		d['diploma'] = m[6][1:-1].replace(' ','')
		d['degree'] = m[7][1:-1].replace(' ','')
		d['email'] = m[8][1:-1].replace(' ','')
	except IndexError as e:
		print(d['id'], d['campus'], e)
	return d

if __name__ == '__main__':

	s_time = time.time()
	infos = get_info()

	headers = []
	for k in extract_info(infos[0]).keys():
		headers.append(k)

	td_file = 'td.csv'
	csv_in = open(td_file, 'w+', encoding = 'gbk')
	cw = csv.DictWriter(csv_in, fieldnames = headers)
	cw.writeheader()
		
	for i,uinfo in enumerate(sorted(set(infos))):
		d = extract_info(uinfo)
		cw.writerow(d)
		#print(d)
	csv_in.close()
	
	e_time = time.time()
	elapsed_time = e_time - s_time
	print('Time elapsed: {0:.2f} seconds.'.format(elapsed_time))
