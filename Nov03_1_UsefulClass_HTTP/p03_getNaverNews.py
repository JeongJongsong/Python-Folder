# https://developers.naver.com/main/

# 애플리케이션 등록
#   애플리케이션 이름 : 마음대로
#   사용API : 검색
#   비로그인 .. : WEBB설정 -> 웹사이트 주소 아는거 아무거나
# ClientID : chC79QmHu050wMPQuSAa
# ClientSecret :  WpdqLU4laG

# request parameter
#   클라이언트가 서버에게 전달하는 정보
#   주소 뒤에 전달됨
# request header
#   클라이언트가 서버에게 전달하는 정보
#   주소 뒤에 
#   내부적으로 전달됨


# 인터넷 주소 체계                      생략가능
#   http or https(프로토콜)://서버주소[:포트번호]/폴더/폴더.../파일
#   주소뒤에 ? -> 변수명=값&변수명=값&변수명=값...
#   https://opnapi.naver.com/v1/search/news.xml?

# 인터넷 주소에 한글, 특수문자 안됨!!
#   한글, 특수문자를 -> %2A(URL인코딩) 이런형태로 바꿔 넣어야함

# 실시간 네이버 뉴스를 AI훈련용 데이터로 확하는 프로그램
# 1) HTTP통신해서 콘솔출력
# 2) 파싱 -> title, description -> 콘솔출력
# 3) 날짜, title, decription -> 파일에 저장



from datetime import datetime
from http.client import HTTPSConnection
from urllib.parse import quote
from xml.etree.ElementTree import fromstring
from jeong.jeongStringCleaner import jeongStringCleaner

q = "해외스포츠"
q = quote(q) # URL인코딩 해주는것

k = {"X-Naver-Client-Id" : "chC79QmHu050wMPQuSAa",
     "X-Naver-Client-Secret" : "WpdqLU4laG"}

hc = HTTPSConnection("openapi.naver.com")
hc.request("GET", "/v1/search/news.xml?query="+q, headers=k)
res = hc.getresponse()
resBody = res.read()
print(resBody.decode())
hc.close()
####################################################

f = open("C:/Users/soldesk/Desktop/naverNews.txt", "a", encoding="utf-8")
newsData = fromstring(resBody)
news = newsData.iter("item")
now = datetime.today()
now = datetime.strftime(now, "%Y\t%m\t%d\t%H\t%M")
for n in news:
    title = (jeongStringCleaner.clean(n.find("title").text))
    dectiption = (jeongStringCleaner.clean(n.find("description").text))
    data = "%s,%s,%s\t" %(now, title, dectiption)
    f.write(data)

f.close()