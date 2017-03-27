# Project Euler Crawler
# Python 2
import urllib
import urllib2

def PEC(number):
    url = "https://projecteuler.net/"
    data = {'problem': number}
    request = urllib2.request(url, data)
    response = urllib2.urlopen(request)
    result = response.read()
    ext = '.html'
    filename = str(number) + ext
    f = open(filename, 'w')
    f.write(result)
    print(filename + " downloaded")
    f.close()

numbers = range(1, 505)

for i in numbers:
	PEC(i)
