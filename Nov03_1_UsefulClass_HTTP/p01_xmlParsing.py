# AI 훈련용 데이터
#   1) 직접만들
#   2) 인터넷에서 구해
#       csv파일
#       xml/json
#       ...
######################
# 포털사이트
# 정부사이트
# SNS

# 미세먼지-> 공공데이터 더보기 ->

# HTTP통신 걸어서 -> 콘솔창에 출력

# XML(eXtended Markup Language)
#   데이터를 HTML모양으로 표현해놓은것
#   HTML -> DOM(Document Object Model)객체모양으로 
#       <TagName attribute ="value" ...> : stratTag
#       text                             : text
#       </tagName>                       : endTag
#       <MSRDT>202511030900</MSRDT>
#       <시작Tag>  text    <endTag>

# http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/xml/RealtimeCityAir/1/5/

from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring


hc = HTTPConnection("openapi.seoul.go.kr:8088")
hc.request("GET", "/575a4655496b636839386f58586542/xml/RealtimeCityAir/1/25/")
res = hc.getresponse()
resBody = res.read()
hc.close()
#########################################################
seoluDustDataa = fromstring(resBody) # xml파싱시작
rowsss = seoluDustDataa.iter("row") # <row></row>들 / iter -> 여러개 찾을때 사용
for r in rowsss:
    print(r.find("MSRRGN_NM").text)     # <MSRRGN_NM></MSRRGN_NM>    / find -> 하나 찾을때 사용
    print(r.find("MSRSTE_NM").text)
    print(r.find("PM10").text)
    print(r.find("PM25").text)
    print(r.find("IDEX_NM").text)
print("-----------------------------")