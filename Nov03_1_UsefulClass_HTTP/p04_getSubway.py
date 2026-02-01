# getSubway
# data.seoul.go.kr
#   지하철 -> 서울시 지하철호선별 역별 승하차 인원 정보
#   Open API
#   http://openapi.seoul.go.kr:8088/(인증키)/xml/CardSubwayStatsNew/1/5/20151101
#  2015/01/01 ~ 2024/12/31
#   subway.csv

from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring


f = open("C:/Users/soldesk/Desktop/Jeongjs/subway.csv", "a", encoding="utf-8")
hc = HTTPConnection("openapi.seoul.go.kr:8088")
for yy in range(2015,2025):
    for mm in range(1,13):
        for dd in range(1, 32):
            when = "%d%02d%02d" % (yy, mm, dd)
            hc.request("GET", "/575a4655496b636839386f58586542/xml/CardSubwayStatsNew/1/630/" + when)
            resBody = hc.getresponse().read()
    
            subwayData = fromstring(resBody)
            rows = subwayData.iter("row")

            for s in rows:
                use_ymd = s.find("USE_YMD").text
                y = use_ymd[0:4]
                m= use_ymd[4:6]
                d = use_ymd[6:8]
                routName = s.find("SBWY_ROUT_LN_NM").text.replace(",", ".")
                stationName = s.find("SBWY_STNS_NM").text.replace(",", ".")
                getOn = s.find("GTON_TNOPE").text
                getOff = s.find("GTOFF_TNOPE").text
                data = "%s,%s,%s,%s,%s,%s,%s\n" %(y,m,d,routName,stationName,getOn,getOff)
                f.write(data)
            print(when)
#######################################################
hc.close()
f.close()
