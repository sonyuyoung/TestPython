import bs4
import urllib.request
import csv

# 알라딘   -> csv

# 함수 선언부
def getBookInfo(book_tag):
    img_tag = book_tag.find("img")
    img_tag_src = img_tag['src'] if img_tag and 'src' in img_tag.attrs else 'Unknown Image'

    names = book_tag.find("div", {"class": "b-author"})
    authorName = names.text if names else 'Unknown Author'

    # 가격 
    price = book_tag.find("div", {"class": "b-price"})
    price2 = price.find("strong") if price else None
    price3 = price2.text if price2 else 'Unknown Price'
    
    # 책제목 
    title_tag = book_tag.find("a")
    title = title_tag.text if title_tag else 'Unknown Title'

    return [title, authorName, price3, img_tag_src]

# 전역 변수부
# url = "http://www.yes24.com/24/Category/Display/001001003022004?ParamSortTp=05&PageNumber="
# pageNumber = 1
url = "https://www.aladin.co.kr/shop/wbrowse.aspx?CID=2551"
# 전체 리스트 
result_list = []

# 메인 코드부
csvName = '/Users/u020/TestPython/ch9_crawling1/aladinBook.csv'
with open(csvName, 'w', newline='',encoding='UTF-8') as csvFp:
    csvWriter = csv.writer(csvFp)
    csvWriter.writerow(['책이름', '저자', '가격','책커버이미지'])

    # 초기셋팅 페이지 없고, 하나만들고온 
    htmlObject = urllib.request.urlopen(url)
    webPage = htmlObject.read()
    bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
    

    tag = bsObject.find('ul', {'class': 'b-booklist BrowseBestSeller'})
    # 구조 일반 이미지 : <div class="b-cover">,
    all_books_Img = tag.findAll('div', {'class': 'b-cover'})
        # 일반 텍스트  : <div class="b-text">
    all_books_Txt = tag.findAll('div', {'class': 'b-text'})

        # # 이미지 주소만 가져오기. 
        # for book in all_books_Img:
        #     bookImg = getBookInfoImg(book)
        #     bookImgTxt = bookImg[0]
        #     result_list.append(bookImgTxt)
        #  # 저자, 가격 가져오기. 
        # for book in all_books_Txt:
        #     bookTxt = getBookInfoTxt(book)
        #     bookName = bookTxt[0]
        #     result_list.append(bookName)
        #     bookAuthor = bookTxt[1]
        #     result_list.append(bookAuthor)
        #     bookPrice = bookTxt[2]
        #     result_list.append(bookPrice)

        # 이미지 주소만 가져오기. 
    for book in zip(all_books_Img, all_books_Txt):
        bookImg = getBookInfo(book[0])
        result_list.extend(bookImg)
        bookTxt = getBookInfo(book[1])
        result_list.extend(bookTxt)

    csvWriter.writerow(result_list)


    #     # 저자, 가격 가져오기. 
    # for book in all_books_Txt:
    #         bookTxt = getBookInfoTxt(book)
    #         result_list.extend(bookTxt)

        # for book in result_list:
        #     info_list = getBookInfo(book)
    print(f"result_list : {result_list}")
    with open(csvName, 'a', newline='',encoding="UTF-8") as csvFp:
            csvWriter = csv.writer(csvFp)
            csvWriter.writerow(result_list)



print('Save. OK~')
