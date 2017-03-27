# LaborBob.py
# Execute commands in ProjectEulerCrawler

import ProjectEulerCrawler

__author__ = 'Libao Jin'
__date__ = 'June 17, 2015'

path = '../Problems/rawpages/'
loc = '../Problems/rawpages/'
ext = '.html'

numbers = range(465, 505)

#for i in numbers:
	#ProjecEulerCrawler.PEC(numbers)

result = ProjectEulerCrawler.ExtractContent(40, path, ext)
pages = result[0]
abnormal = result[1]
print('\n' + 40*'*' + ' pages ' + 40*'*' + '\n')
print(pages)
print('\n' + 40*'*' + ' abnor ' + 40*'*' + '\n')
print(abnormal)

inputfile = '../Problems/basic.htm'
outputfile = '../Problems/All.Problems-Project.Euler.html'
ProjectEulerCrawler.MergeContents(pages, inputfile, outputfile)
print('Captain, mission accomplished!')
