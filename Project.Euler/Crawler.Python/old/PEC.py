# Project Euler Crawler
# Python 3
import urllib.parse
import urllib.request

def PEC(number):
	basic_url = "https://projecteuler.net/problem="
	url = basic_url + str(number)
	request = urllib.request.Request(url)
	response = urllib.request.urlopen(request)
	result = response.readall().decode('utf-8')
	loc = '../Problems/pages/'
	ext = '.html'
	filename = loc + str(number) + ext
	f = open(filename, 'w')
	f.write(result)
	print(filename + " downloaded")
	f.close()

numbers = range(465, 505)

for i in numbers:
	PEC(i)
