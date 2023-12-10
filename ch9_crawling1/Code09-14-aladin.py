import bs4
import urllib.request
# 알라딘 특정 , 도서 정보를 가져오기. 콘솔 출력. 특정 한페이지만

# 함수 선언부
def getBookInfoImg(book_tag):
    img_tag = book_tag.find("img")
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

    return [title,authorName, price3]
# 전역 변수부
# 해당 사이트의 하위 주소 부분 반드시 조사.
# https://www.yes24.com/24/Category/Display/001001003022?ParamSortTp=05&PageNumber=2
# bookUrl = "http://www.yes24.com/24/Category/Display/001001046001?ParamSortTp=05&PageNumber=1"
bookUrl = "https://www.aladin.co.kr/shop/wbrowse.aspx?CID=2551"
# 메인 코드부
# 가독성
htmlObject = urllib.request.urlopen(bookUrl)
webPage = htmlObject.read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

# 태그 의 트리 구조 조사 , 정보 접근하기.
# (.) 점 : 클래스 의미, # : 아이디 의미.
# ul : .clearfix ->
# ul : .clearfix -> div : .goods_info , 모든 값을 리스트에 담기.
tag = bsObject.find('ul', {'class': 'b-booklist BrowseBestSeller'})
# 일반 이미지와 일반텍스트 나누어져있꼬 b-cover b-text
# 구조 일반 이미지 : <div class="b-cover">,
all_books_Img = tag.findAll('div', {'class': 'b-cover'})

# 일반 텍스트  : <div class="b-text">
all_books_Txt = tag.findAll('div', {'class': 'b-text'})

# 여기 리스트에 해당책의 1)a링크 , 2) 이미지 주소 
# 이미지 주소만 가져오기 . 
for book in all_books_Img:
    print(getBookInfoImg(book))

# 저자, 가격 가져오기. 
for book in all_books_Txt:
    print(getBookInfoTxt(book))

#     <div class="b-bestseller">
#     <div class="b-tt">
#         <h3><a href="/shop/common/wbest.aspx?BranchType=1&BestType=Bestseller&CID=2551">화제의 <em>베스트셀러</em></a></h3>
#         <ul id="BestTab">
#             <li class="on"><a href="javascript:void(0);">주간 베스트</a></li><li><a href="javascript:void(0);">신간 베스트</a></li>
#         </ul>
#     </div>
#     <ul class="b-booklist BrowseBestSeller" >
#     <li><div class="b-cover"><em>1위</em>
#     <a href="https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=330062247">
#     <img src="https://image.aladin.co.kr/product/33006/22/cover/k792937873_1.jpg" border="0">
#     </a>
#     </div>
#     <div class="b-text">
#     <h4><a href="https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=330062247">
#     주술회전 24 (초판한정 후시구로 메구미 일러스트 카드 + 선착순 한정 이타도리’&‘고죠 빅 스티커 포함 특장판)</a></h4>
#     <div class="b-author">아쿠타미 게게 지음, 이정운 옮김 | 서울미디어코믹스(서울문화사)</div>
#     <div class="b-price"><strong>5,400</strong>원 / 300원</div></div></li>
#     <li>
#     <div class="b-cover">
#     <em>2위</em><a href="https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=330062003">
#     <img src="https://image.aladin.co.kr/product/33006/20/cover/k682937873_1.jpg" border="0"></a></div>
#     <div class="b-text"><h4><a href="https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=330062003">주술회전 24 + 2024 캘린더 세트 (한정판)</a></h4>
#     <div class="b-author">아쿠타미 게게 지음, 이정운 옮김 | 서울미디어코믹스(서울문화사)</div><div class="b-price"><strong>24,300</strong>원 / 1,350원
#     </div>
#     </div></li>
#     <li><div class="b-cover"><em>3위</em>
#     <a href="https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=330028236">
#     <img src="https://image.aladin.co.kr/product/33002/82/cover/k412937775_1.jpg" border="0"></a></div><div class="b-text"><h4><a href="https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=330028236">블루 아카이브 흥신소 68 업무일지 1</a></h4><div class="b-author">Nogiwa Kaede 지음, 심이슬 옮김, 블루 아카이브 원작 | 서울미디어코믹스(서울문화사)</div><div class="b-price"><strong>8,100</strong>원 / 450원</div></div></li><li><div class="b-cover"><em>4위</em><a href="https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=330009859"><img src="https://image.aladin.co.kr/img/19book_200cover.jpg" border="0"></a></div><div class="b-text"><h4><a href="https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=330009859">위험한 편의점 시즌3 스페셜 패키지 - 전2권 (완결)</a></h4><div class="b-author">945 지음 | blackD(블랙디)</div><div class="b-price"><strong>48,600</strong>원 / 2,700원</div></div></li><li><div class="b-cover"><em>5위</em><a href="https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=329751704"><img src="https://image.aladin.co.kr/product/32975/17/cover/k762936559_1.jpg" border="0"></a></div><div class="b-text"><h4><a href="https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=329751704">망그러진 만화 2</a></h4><div class="b-author">유랑 지음 | 좋은생각</div><div class="b-price"><strong>15,750</strong>원 / 870원</div></div></li><li><div class="b-cover"><em>6위</em><a href="https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=329703434"><img src="https://image.aladin.co.kr/product/32970/34/cover/k022936356_1.jpg" border="0"></a></div><div class="b-text"><h4><a href="https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=329703434">지박소년 하나코 군 20 (한정판)</a></h4><div class="b-author">아이다이로 지음, 장혜영 옮김 | 서울미디어코믹스(서울문화사)</div><div class="b-price"><strong>14,400</strong>원 / 800원</div></div></li><li><div class="b-cover"><em>7위</em><a href="https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=329643642"><img src="https://image.aladin.co.kr/product/32964/36/cover/k852936251_1.jpg" border="0"></a></div><div class="b-text"><h4><a href="https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=329643642">나의 히어로 아카데미아 39 (한정판)</a></h4><div class="b-author">호리코시 코헤이 지음 | 서울미디어코믹스(서울문화사)</div><div class="b-price"><strong>5,400</strong>원 / 300원</div></div></li><li><div class="b-cover"><em>8위</em><a href="https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=329703592"><img src="https://image.aladin.co.kr/product/32970/35/cover/k252936356_1.jpg" border="0"></a></div><div class="b-text"><h4><a href="https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=329703592">지박소년 하나코 군 20</a></h4><div class="b-author">아이다이로 지음, 장혜영 옮김 | 서울미디어코믹스(서울문화사)</div><div class="b-price"><strong>5,400</strong>원 / 300원</div></div></li></ul><ul class="b-booklist BrowseBestSeller" style="display:none;"><li><div class="b-cover"><em>1위</em><a href="https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=330062247"><img src="https://image.aladin.co.kr/product/33006/22/cover/k792937873_1.jpg" border="0"></a></div><div class="b-text"><h4><a href="https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=330062247">주술회전 24 (초판한정 후시구로 메구미 일러스트 카드 + 선착순 한정 이타도리’&‘고죠 빅 스티커 포함 특장판)</a></h4><div class="b-author">아쿠타미 게게 지음, 이정운 옮김 | 서울미디어코믹스(서울문화사)</div><div class="b-price"><strong>5,400</strong>원 / 300원</div></div></li><li><div class="b-cover"><em>2위</em><a href="https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=330062003"><img src="https://image.aladin.co.kr/product/33006/20/cover/k682937873_1.jpg" border="0"></a></div><div class="b-text"><h4><a href="https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=330062003">주술회전 24 + 2024 캘린더 세트 (한정판)</a></h4><div class="b-author">아쿠타미 게게 지음, 이정운 옮김 | 서울미디어코믹스(서울문화사)</div><div class="b-price"><strong>24,300</strong>원 / 1,350원</div></div></li><li><div class="b-cover"><em>3위</em><a href="https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=330028236"><img src="https://image.aladin.co.kr/product/33002/82/cover/k412937775_1.jpg" border="0"></a></div><div class="b-text"><h4><a href="https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=330028236">블루 아카이브 흥신소 68 업무일지 1</a></h4><div class="b-author">Nogiwa Kaede 지음, 심이슬 옮김, 블루 아카이브 원작 | 서울미디어코믹스(서울문화사)</div><div class="b-price"><strong>8,100</strong>원 / 450원</div></div></li><li><div class="b-cover"><em>4위</em><a href="https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=330009859"><img src="https://image.aladin.co.kr/img/19book_200cover.jpg" border="0"></a></div><div class="b-text"><h4><a href="https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=330009859">위험한 편의점 시즌3 스페셜 패키지 - 전2권 (완결)</a></h4><div class="b-author">945 지음 | blackD(블랙디)</div><div class="b-price"><strong>48,600</strong>원 / 2,700원</div></div></li><li><div class="b-cover"><em>5위</em><a href="https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=329751704"><img src="https://image.aladin.co.kr/product/32975/17/cover/k762936559_1.jpg" border="0"></a></div><div class="b-text"><h4><a href="https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=329751704">망그러진 만화 2</a></h4><div class="b-author">유랑 지음 | 좋은생각</div><div class="b-price"><strong>15,750</strong>원 / 870원</div></div></li><li><div class="b-cover"><em>6위</em><a href="https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=329775325"><img src="https://image.aladin.co.kr/product/32977/53/cover/k212936554_1.jpg" border="0"></a></div><div class="b-text"><h4><a href="https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=329775325">망그러진 만화 2 + 망그러진 하루 Daily book 세트 - 전2권</a></h4><div class="b-author">유랑 지음 | 좋은생각</div><div class="b-price"><strong>22,950</strong>원 / 1,270원</div></div></li><li><div class="b-cover"><em>7위</em><a href="https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=330006545"><img src="https://image.aladin.co.kr/product/33000/65/cover/k532937778_1.jpg" border="0"></a></div><div class="b-text"><h4><a href="https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=330006545">악마에 입문했습니다! 이루마 군 12</a></h4><div class="b-author">니시 오사무 지음, 이승원 옮김 | 서울미디어코믹스(서울문화사)</div><div class="b-price"><strong>5,850</strong>원 / 320원</div></div></li><li><div class="b-cover"><em>8위</em><a href="https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=330006596"><img src="https://image.aladin.co.kr/product/33000/65/cover/k642937778_1.jpg" border="0"></a></div><div class="b-text"><h4><a href="https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=330006596">악마에 입문했습니다! 이루마 군 13</a></h4><div class="b-author">니시 오사무 지음, 이승원 옮김 | 서울미디어코믹스(서울문화사)</div><div class="b-price"><strong>5,850</strong>원 / 320원</div></div></li></ul>
# </div>

#  a_tag = li.find("a")
#     print(f"a_tag 결과: {a_tag}")
#     a_tag_href = a_tag['href']