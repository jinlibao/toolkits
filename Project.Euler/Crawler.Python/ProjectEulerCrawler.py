# ProjectEulerCrawler.py
# Project Euler Crawler
# Combine webpages into one page

import urllib.parse
import urllib.request
import re

__author__ = 'Libao Jin'
__date__ = 'June 17, 2015'

def ExtractContent(number, path, ext):
	n = range(1,number)
	# store problem content in pages (dict)
	pages = {}
	# store abnormal content in abnormal (dict, which cannot be
	# matched, mainly in order to find bugs) 
	abnormal = {}
	for i in n:
		print(i)
		# generate filename
		rfile = path + str(i) + ext
		# open and read file
		r = open(rfile, 'r')#, encoding = 'utf-8')
		page = r.read()
		# find desired contents using regular expression, say, re module
		question_pattern = re.compile('<div id="content">.*(\n+.*)*<br /></div>')
		all_pattern = re.compile('<div id="content">.*(\n+.*)*')
		question = re.search(question_pattern, page)
		all_ = re.search(all_pattern, page)
		if question is not None:
			contents = question.group()
			# remove images
			img_pattern =  re.compile('<img src.*/>')
			imgless_contents =  re.sub(img_pattern, ' ', contents)
			pages[str(i)] = imgless_contents
		else:
			print('pattern not found.')
			if all_ is not None:
				print('\n' + 40*'*' + ' patter2 ' + 40*'*' + '\n')
				print(all_.group())
				abnormal[str(i)] = all_.group()
	return [pages,abnormal]
	r.close()

def MergeContents(pages, inputfile, outputfile):

	r = open(inputfile, 'r', encoding = 'utf-8')
	rawpage = r.read()
	w = open(outputfile, 'w', encoding = 'utf-8')

	contents = ''
	length = len(pages)
	n = range(1,length+1)
	for i in n:
		if pages.__contains__(str(i)):
			contents = contents + '\n' + pages[str(i)]
		else:
			print(str(i) + 'does not exist.')
	pattern = 'DIYCONTENTS'
	newpage = re.sub(pattern, contents, rawpage)
	w.write(newpage)
	r.close()
	w.close()

def PEC(number, loc, ext):
	basic_url = "https://projecteuler.net/problem="
	url = basic_url + str(number)
	request = urllib.request.Request(url)
	response = urllib.request.urlopen(request)
	result = response.readall().decode('utf-8')
	filename = loc + str(number) + ext
	f = open(filename, 'w')
	f.write(result)
	print(filename + " downloaded")
	f.close()
