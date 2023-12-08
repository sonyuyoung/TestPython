import os
import bs4

webPage = open('/Users/u020/TestPython/ch9_crawling1/Sample02.html',
               'rt', encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

# 특정 태그를 찾는 연습.
tag_div = bsObject.find('div')
print(tag_div)
