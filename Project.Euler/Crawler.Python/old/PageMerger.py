# Project Euler Page Merger
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

def MergeContents(pages):
	contents = ''
	length = len(pages)
	n = range(1,length+1)
	for i in n:
		if pages.__contains__(str(i)):
			contents = contents + '\n' + pages[str(i)]
		else:
			print(str(i) + 'does not exist.')
	return contents

path = '../Problems/rawpages/'
ext = '.html'
result = ExtractContent(487, path, ext)
pages = result[0]
abnormal = result[1]
print('\n' + 40*'*' + ' pages ' + 40*'*' + '\n')
print(pages)
print('\n' + 40*'*' + ' abnor ' + 40*'*' + '\n')
print(abnormal)

rbasic = '../Problems/basic.htm'
r = open(rbasic, 'r', encoding = 'utf-8')
rawpage = r.read()
pattern = 'DIYCONTENTS'
contents = MergeContents(pages)
m = re.sub(pattern, contents, rawpage)
wfile = '../Problems/All.Problems-Project.Euler.html'
w = open(wfile, 'w', encoding = 'utf-8')
w.write(m)
