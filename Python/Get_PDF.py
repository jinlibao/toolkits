#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Libao Jin'
__create_date__ = '06/02/2017'
__copyright__ = 'Copyright (c) 2017 Libao Jin'
__email__ = 'jinlibao@outlook.com'
__status__ = 'In progress'
__version__ = '0.1'

import os
# os.environ['http_proxy'] = ''
import urllib.request
import urllib.error
import re

class Get_PDF():
    '''
    Get_PDF: General purpose PDF retriever
    '''

    def __init__(self, loc='.', ext='pdf', is_replacing=True):
        self.loc = loc
        self.ext = ext
        self.is_replacing = is_replacing

    def get_html(self):
        url = self.url
        # print(url)
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
        host = 'www.cs.cmu.edu'
        connection = 'Keep-Alive'
        accept = 'text/html, application/xhtml+xml, image/jxr, */*'
        accept_encoding = 'gzip, deflate'
        accept_language = 'en-US, en; q=0.5'
        cookie = 'has_js=1; _pk_id.2.8275=dd62bf93cfb11e12.1496439140.1.1496439164.1496439140.; _bizo_bzid=1eaf0a76-35ae-452a-87b8-934e71b27940; _bizo_cksm=C3B6BD528E033D70; _bizo_np_stats=155%3D268%2C1640%3D263%2C; __utmc=44984886; _ga=GA1.2.1884141648.1496439133; _gid=GA1.2.540592622.1496439133; __utma=44984886.1607646947.1496439133.1496439133.1496439133.1; __utmz=44984886.1496439133.1.1.utmccn=(direct)|utmcsr=(direct)|utmcmd=(none); SHIBLOCATION=local'
        headers = {'User-Agent': user_agent,
                   'Host': host,
                   'Connection': connection,
                   'Accept': accept,
                   'Accept-Encoding': accept_encoding,
                   'Accept-Language': accept_language,
                   'Cookie': cookie}
        # print(headers)
        req = urllib.request.Request(url, headers = headers)
        try:
            with urllib.request.urlopen(req) as  response:
                html_content = response.read()
                # print(html_content)
                self.html = html_content.decode('utf-8')
        except urllib.error.URLError as e:
            print(e)

    def extract_urls(self):
        html = self.html
        ext = self.ext
        # print(html)
        # pattern = '/([\w\d\s.-]+.{0})'.format(ext)
        pattern = '([\w\d\s/.-]+/([\w\d\s.-]+).{0})'.format(ext)
        p = re.compile(pattern)
        urls = p.findall(html)
        print(urls)
        self.urls = urls

    def save_files(self):
        for url in self.urls:
            url_suffix, name = url
            file_url = self.site_url + url_suffix
            filename = r'{0}/{1}.{2}'.format(self.loc, name, self.ext)
            if not self.is_replacing:
                filename_tmp = filename
                file_number = 0
                while os.path.exists(filename_tmp):
                    file_number = file_number + 1
                    filename_tmp = r'{0}/{1}-{2}.{3}'.format(self.loc, name, str(file_number).zfill(2), self.ext)
                    # print(filename_tmp)
                filename = filename_tmp
            print('{0}, {1}'.format(file_url, filename))
            try:
                urllib.request.urlretrieve(file_url, filename)
            except urllib.error.URLError as e:
                print(e)

    def collect_pdf_urls(self):
        self.get_html()
        self.extract_urls()
        self.save_files()


    def go(self, url, site_url):
        self.url = url
        self.site_url = site_url
        self.collect_pdf_urls()

if __name__ == '__main__':
    Tom = Get_PDF()
    Tom.go(url='http://www.cs.cmu.edu/~15150/lect.html', site_url='http://www.cs.cmu.edu/~15150/')
