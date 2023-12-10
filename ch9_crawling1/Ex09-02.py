import bs4
import urllib.request
import csv

# 알라딘 -> csv

# 함수 선언부


# 함수 선언부
def getBookInfoImg(book_tag):
    img_tag = book_tag.find("img")
    if img_tag:
        img_tag_src = img_tag['src']
        return [img_tag_src]

# 하위에 이미지 하나만 가져오는 테스트
# 저자, 가격 가져오기.
# 제목을 가져올건데 b-text -
def getBookInfoTxt(book_tag):
    # 저자
    names = book_tag.find("div", {"class": "b-author"})
    authorName = names.text
    # 가격
    price = book_tag.find("div", {"class": "b-price"})
    price2 = price.find("strong")
    price3 = price2.text
    # 책제목
    # title = book_tag.find("div", {"class": "b-author"})
    # title = names.find("h4")
    title = book_tag.find("a").text

    return [title, authorName, price3]

# 수정, 각각 함수를 하나로 변경.
def getBookInfoTotal(book_tag, book_tag2):
    # 저자
    names = book_tag.find("div", {"class": "b-author"})
    authorName = names.text
    # 가격
    price = book_tag.find("div", {"class": "b-price"})
    price2 = price.find("strong")
    price3 = price2.text
    # 책 제목
    bookName = book_tag.find("a").text

    # 책 이미지
    img_tag = book_tag2.find("img")
    # print(f"img_tag 결과: {img_tag}")
    img_tag_src = img_tag['src']

    return [bookName, authorName, price3, img_tag_src]


# 전역 변수부
# url = "http://www.yes24.com/24/Category/Display/001001003022004?ParamSortTp=05&PageNumber="
# pageNumber = 1
url = "https://www.aladin.co.kr/shop/wbrowse.aspx?CID=2551"

# 이미지 리스트
img_list = []

# 일반텍스트 리스트
txt_list = []

# 전체 리스트
result_list = []

# 메인 코드부
# CSV 파일 생성
csvName = '/Users/u020/TestPython/ch9_crawling1/aladinBook.csv'
with open(csvName, 'w', newline='', encoding='UTF-8') as csvFp:
    csvWriter = csv.writer(csvFp)
    csvWriter.writerow(['책이름', '저자', '가격', '책커버이미지'])


# 무한 루프를 돌며 도서 정보를 스크래핑하고 CSV 파일에 저장
i = 0

while True:
    try:
        # 초기세팅
        htmlObject = urllib.request.urlopen(url)
        webPage = htmlObject.read()
        bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

        tag = bsObject.find('ul', {'class': 'b-booklist BrowseBestSeller'})
        # 구조 일반 이미지 : <div class="b-cover">,
        all_books_Img = tag.findAll('div', {'class': 'b-cover'})

         # 일반 텍스트  : <div class="b-text">
        all_books_Txt = tag.findAll('div', {'class': 'b-text'})

         # 이미지 주소만 가져오기. 
        for book in all_books_Img:
            bookImg = getBookInfoImg(book)
            bookImgTxt = bookImg[0]
            img_list.append(bookImgTxt)
            # result_list.append(bookImgTxt)

        # 책제목, 저자, 가격 가져오기. 
        for book in all_books_Txt:
            bookTxt = getBookInfoTxt(book)
            txt_list.append(bookTxt)
            # txt_list.append(bookTxt)
            # bookName = bookTxt[0]
            # txt_list.append(bookName)
            # bookAuthor = bookTxt[1]
            # txt_list.append(bookAuthor)
            # bookPrice = bookTxt[2]
            # txt_list.append(bookPrice)
        
        # img_list -> 사진 1장 url , 
        # txt_list -> [책제목,저자,가격]
        # result_list -> 

        for txt in txt_list:
            bookName = txt[0]
            result_list.append(bookName)
            bookAuthor = txt[1]
            result_list.append(bookAuthor)
            bookPrice = txt[2]
            result_list.append(bookPrice)
            # 사진 한장 뿐
            result_list.append(img_list[i])
            i = i+1

             # for book in result_list:
        #     info_list = getBookInfo(book)
        print(f"result_list : {result_list}")
       
        # 4개씩 끊어서 CSV 파일에 작성
         # 쓰기 잠시 대기. -> 4개씩 끊어서 쓰기 작업. 
        chunked_data = [result_list[i:i+4] for i in range(0,len(result_list),4)]
        for result in chunked_data:
            with open(csvName, 'a', newline='',encoding="UTF-8") as csvFp:
                csvWriter = csv.writer(csvFp)
                csvWriter.writerow(result)

            
    except:
        break

print('Save. OK~')
