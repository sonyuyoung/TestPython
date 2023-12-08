import bs4
import urllib.request
import csv

# 알라딘   -> csv
# 함수 선언부
def getBookInfo(book_tag):
    # 이미지
    img_tag = book_tag.find("img")
    img_url = img_tag['src']

    # 텍스트 정보
    text_tag = book_tag.find("div", {"class": "b-text"})
    # 제목
    title = text_tag.find("a").text
    # 작가
    author_tag = text_tag.find("div", {"class": "b-author"})
    author = author_tag.text
    # 가격
    price_tag = text_tag.find("div", {"class": "b-price"})

    price = price_tag.find("strong").text.replace(",", "")

    return [title, author, price, img_url]
# 전역 변수부
# url = "http://www.yes24.com/24/Category/Display/001001003022004?ParamSortTp=05&PageNumber="
# pageNumber = 1
url = "https://www.aladin.co.kr/shop/wbrowse.aspx?CID=2551"
# 전체 리스트 
result_list = []
# 메인 코드부
csvName = '/Users/u020/TestPython/ch9_crawling1/aladinBook.csv'
with open(csvName, 'w', newline='', encoding='UTF-8') as csvFp:
    csvWriter = csv.writer(csvFp)
    csvWriter.writerow(['책이름', '저자', '가격', '책커버이미지'])

    # 초기셋팅 페이지 없고, 하나만들고온
    htmlObject = urllib.request.urlopen(url)
    webPage = htmlObject.read()
    bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

    bestseller_div = bsObject.find('div', {'class': 'b-bestseller'})
    all_books = bestseller_div.select('ul.b-booklist.BrowseBestSeller > li')

    for book in all_books:
        book_info = getBookInfo(book)
        result_list.extend(book_info)

    # Write the result_list to CSV
    csvWriter.writerow(result_list)

print('Save. OK~')