#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Libao Jin'
__create_date__ = '06/02/2017'
__update_date__ = '01/07/2019'
__copyright__ = 'Copyright (c) 2017-2018 Libao Jin'
__email__ = 'jinlibao@outlook.com'
__status__ = 'Complete'
__version__ = '0.2'

import gzip
import io
import os
import re
import urllib.request
import urllib.error

class Get_PDF():
    '''
    Get_PDF: General purpose PDF retriever
    '''

    def __init__(self, host, course_number='15418', loc='.', ext='pdf', is_replacing=True):
        self.host = host
        self.course_number = course_number
        self.loc = loc
        self.ext = ext
        self.is_replacing = is_replacing
        self.urls = []

    def get_html(self, url):
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        host = self.host
        connection = 'keep-alive'
        accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
        accept_encoding = 'gzip, deflate'
        accept_language = 'en,en-US;q=0.9'
        cookie = '_ga=GA1.2.245434328.1546131362; _gid=GA1.2.441993721.1546131362; BIGipServer~SCS~cs-userdir-pool-80=2748908160.20480.0000; BIGipServer~SCS~cs-userdir-pool-443=2748908160.47873.0000; SHIBLOCATION=local'
        headers = {'User-Agent': user_agent,
                   'Host': host,
                   'Connection': connection,
                   'Accept': accept,
                   'Accept-Encoding': accept_encoding,
                   'Accept-Language': accept_language,
                   'Cookie': cookie,
                   }
        # print(headers)
        self.headers = headers
        req = urllib.request.Request(url, headers = headers)
        try:
            with urllib.request.urlopen(req) as  response:
                html_content = response.read()
                if len(html_content) > 2 and html_content[0] == 31 and html_content[1] == 139:
                    buf = io.BytesIO(html_content)
                    f = gzip.GzipFile(fileobj=buf)
                    html_content = f.read()
                self.html = html_content.decode('utf-8')
        except urllib.error.URLError as e:
            print(e)

    def extract_pages(self):
        html = self.html
        pattern = 'href="(http://[\w\d\s/.-]+/lecture/[\w\d\s/.-]+)"'
        p = re.compile(pattern)
        pages = p.findall(html)
        print(pages)
        for page in pages:
            self.get_html(page)
            self.extract_urls()

    def extract_urls(self):
        html = self.html
        ext = self.ext
        # print(html)
        # pattern = '/([\w\d\s.-]+.{0})'.format(ext)
        # pattern = '([\w\d\s.-]+.{0})'.format(ext)
        pattern = '([\w\d\s/.~-]+/([\w\d\s.-]+).{0})'.format(ext)
        p = re.compile(pattern)
        urls = p.findall(html)
        print(urls)
        self.urls = self.urls + urls

    def save_files(self):
        if not os.path.exists(self.loc):
            os.mkdir(self.loc)
        # self.urls.reverse()
        for url in self.urls:
            if isinstance(url, str):
                file_url = self.site_url + url
                filename = r'{0}/{1}'.format(self.loc, url)
                try:
                    urllib.request.urlretrieve(file_url, filename)
                    print('{0}, {1}, {2}'.format(file_url, filename, 'Downloaded'))
                except urllib.error.URLError as e:
                    print('{}, {}, {}'.format(file_url, filename, e))
            else:
                url_suffix, name = url
                if url_suffix[0:2] == '//':
                    file_url = 'http:' + url_suffix
                elif url_suffix[0:4] == 'http':
                    file_url = url_suffix
                else:
                    file_url = self.site_url + url_suffix
                filename = r'{0}/{1}.{2}'.format(self.loc, name, self.ext)
                # file_url = self.site_url + url
                # filename = r'{0}/{1}'.format(self.loc, url)
                if not self.is_replacing:
                    filename_tmp = filename
                    file_number = 0
                    while os.path.exists(filename_tmp):
                        file_number = file_number + 1
                        filename_tmp = r'{0}/{1}-{2}.{3}'.format(self.loc, name, str(file_number).zfill(2), self.ext)
                        # print(filename_tmp)
                    filename = filename_tmp
                elif os.path.exists(filename):
                    continue
                try:
                    urllib.request.urlretrieve(file_url, filename)
                    print('{0}, {1}, {2}'.format(file_url, filename, 'Downloaded'))
                except urllib.error.URLError as e:
                    print('{}, {}, {}'.format(file_url, filename, e))
                    if url_suffix[0:2] == '//':
                        file_url = 'https:' + url_suffix
                        try:
                            urllib.request.urlretrieve(file_url, filename)
                            print('{0}, {1}, {2}'.format(file_url, filename, 'Downloaded'))
                        except urllib.error.URLError as e:
                            print('{}, {}, {}'.format(file_url, filename, e))

    def go(self, url, site_url, option=1):
        self.url = url
        self.site_url = site_url
        self.get_html(self.url)
        if option == 1:
            self.extract_pages()
        else:
            self.extract_urls()
        self.save_files()


if __name__ == '__main__':
    school = 'CMU'

    # course_number = '15462'  # course_number = '15418'
    # host = '{}.courses.cs.cmu.edu'.format(course_number)
    # semester = 'fall2018'
    # Tom = Get_PDF(host, course_number, '{}.{}.{}'.format(school, course_number, semester))
    # Tom.go(url='http://{}.courses.cs.cmu.edu/{}/'.format(course_number, semester), site_url='http://{}.courses.cs.cmu.edu'.format(course_number), option=1)

    course_number = '15210'  # '15213'  # '15850'  # '15859'  # '411'  # '15251'  # '15451'
    host = 'www.cs.cmu.edu'
    semester = 'fall2018'
    Tom = Get_PDF(host, course_number, '{}.{}.{}'.format(school, course_number, semester))
    # Tom.go(url='https://www.cs.cmu.edu/~{}/index.html'.format(course_number), site_url='http://www.cs.cmu.edu/~{}/'.format(course_number), option=2)
    # Tom.go(url='https://www.cs.cmu.edu/~{}/schedule.html'.format(course_number), site_url='http://www.cs.cmu.edu/~{}/'.format(course_number), option=2)
    # Tom.go(url='http://www.cs.cmu.edu/~janh/courses/{}/18/schedule.html'.format(course_number), site_url='http://www.cs.cmu.edu/~janh/courses/{}/18/'.format(course_number), option=2)
    # Tom.go(url='https://www.cs.cmu.edu/~odonnell/quantum18/', site_url='https://www.cs.cmu.edu/~odonnell/quantum18/', option=2)
    # Tom.go(url='https://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15859-f11/www/', site_url='https://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15859-f11/www/', option=2)
    # Tom.go(url='http://www.cs.cmu.edu/afs/cs/academic/class/15859n-f18/schedule.html', site_url='https://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15859n-f18/', option=2)
    # Tom.go(url='http://www.cs.cmu.edu/~15850/', site_url='http://www.cs.cmu.edu/~15850/', option=2)
    # Tom.go(url='http://www.cs.cmu.edu/~./213/schedule.html', site_url='http://www.cs.cmu.edu/~./213/', option=2)
    # Tom.go(url='https://www.cs.cmu.edu/~15210/schedule.html', site_url='https://www.cs.cmu.edu/~15210/', option=2)
    Tom.go(url='https://www.cs.cmu.edu/~15210/resources/', site_url='https://www.cs.cmu.edu/~15210/', option=2)

    # course_number = '440'
    # host = 'www.synergylabs.org'
    # semester = 'fall2018'
    # Tom = Get_PDF(host, course_number, '{}.{}.{}'.format(school, course_number, semester))
    # Tom.go(url='https://www.synergylabs.org/courses/15-{}/syllabus.html'.format(course_number), site_url='https://www.synergylabs.org/courses/15-{}/'.format(course_number), option=2)

    # course_number = '15-463'
    # host = 'graphics.cs.cmu.edu'
    # semester = 'fall2018'
    # Tom = Get_PDF(host, course_number, '{}.{}.{}'.format(school, course_number, semester), 'zip')
    # Tom.go(url='http://graphics.cs.cmu.edu/courses/{}/'.format(course_number), site_url='http://graphics.cs.cmu.edu/courses/{}/'.format(course_number), option=2)

    # school = 'Washington'
    # course_number = 'CSE.599d'
    # host = 'courses.cs.washington.edu'
    # semester = '2006.Winter'
    # Tom = Get_PDF(host, course_number, '{}.{}.{}'.format(school, course_number, semester))
    # Tom.go(url='https://courses.cs.washington.edu/courses/cse599d/06wi/', site_url='https://courses.cs.washington.edu/courses/cse599d/06wi/', option=2)
