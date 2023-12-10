import bs4
# 실제 사이트에 접근하기 전에,
# 임시 html에서, 각 태그별 접근 연습.
# 해당 url , 특정 html 문서이건 접근하기위한 초기세팅 
webPage = open('/Users/u020/TestPython/ch9_crawling1/Sample02.html',
               'rt', encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

print(bsObject)
