# p01에서 실행하면 실시간 서우 미세먼지 출력하는거 만듦.

# 실행하면 실시간 서울 미세먼지를 csv에 저장
# 2025/11/03 10:52에 실행하면
# 2025/11/03 10:52 서울 미세먼지 출력

# 실행하면 실시간 서울 미세먼지 저장
# 2025,11,03,10,52 도심권,중구,10,5,좋음 
# 2025,11,03,10,52 도심권,종로구,10,5,좋음 
#  ...
# openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/xml/RealtimeCityAir/1/25/
from datetime import datetime
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

hc = HTTPConnection("openapi.seoul.go.kr:8088")
hc.request("GET", "/575a4655496b636839386f58586542/xml/RealtimeCityAir/1/25/")
res = hc.getresponse()
resBody = res.read()
hc.close()
#########################################################

now = datetime.today()
now = datetime.strftime(now, "%Y,%m,%d,%H,%M")

f = open("C:/Users/soldesk/Desktop/jeongjs/seoulDust.csv", "a", encoding="utf-8")
seoluDustDataa = fromstring(resBody) # xml파싱시작
rowsss = seoluDustDataa.iter("row") # <row></row>들 / iter -> 여러개 찾을때 사용
for r in rowsss:
    msrrgn_nm = r.find("SAREA_NM").text     # <MSRRGN_NM></MSRRGN_NM>    / find -> 하나 찾을때 사용
    msrste_nm = r.find("MSRSTN_NM").text
    pm10 = r.find("PM").text
    pm25 = r.find("FPM").text
    index_nm = r.find("CAI_GRD").text
    data = "%s,%s,%s,%s,%s,%s\n" %(now, msrrgn_nm, msrste_nm, pm10, pm25, index_nm)
    f.write(data)

f.close()

