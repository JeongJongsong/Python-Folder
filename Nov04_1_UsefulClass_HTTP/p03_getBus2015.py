# 사울시 버스노선별 정류장별 승하차 인원정보
# Open API
# 첫번째 샘픔URL
# xml -> json

# http://openapi.seoul.go.kr:8088/(인증키)/xml/CardBusStatisticsServiceNew/1/5/20151101/

# bus2015.csv
# bus2016.csv
# bus2017.csv
# ... 1년치씩
# bus2024.csv
# 2015,01,01 ~ 2024,12,31
# 2015,01,01,100번(하계동~용산구청),명륜3가.성대입구,
# ...
from http.client import HTTPConnection
from json import loads

yy = 2024   
f = open("C:/Users/soldesk/Desktop/Jeongjs/bus2024.csv", "a", encoding="utf-8")
hc = HTTPConnection("openapi.seoul.go.kr:8088")
# for yy in range(2015,2025):   -> 이렇게하면 하다가 인터넷 터지면 데이터 못받아와 
for mm in range(1,13):
    for dd in range(1,32):
        for start in range(1,41002, 1000):
            t = "%d%d%d%02d%02d" % (start, start + 999, yy, mm, dd)
            hc.request("GET", "/575a4655496b636839386f58586542/json/CardBusStatisticsServiceNew/1/500/20240101/")
            resBody = hc.getresponse().read()
        
            busData = loads(resBody)
            if "CardBusStatisticsServiceNew" in busData:
                cbssn = busData["CardBusStatisticsServiceNew"]
                stations = cbssn["row"]
            for s in stations:
                uy = s["USE_YMD"] # 2015,11,01 형태로
                y = uy[0:4] # 2015,11,01 형태로
                m= uy[4:6]  # 2015,11,01 형태로
                d = uy[6:8] # 2015,11,01 형태로
                rn = s["RTE_NM"].replace(",", ".") # , 제거
                ssn = s["SBWY_STNS_NM"].replace(",", ".")    # , 제거
                gton = s["GTON_TNOPE"]      # 소수점이하 삭제
                gtoff = s["GTOFF_TNOPE"]    # 소수점이하 삭제
                data = "%s,%s,%s,%s,%s,%.0f,%.0f\n" % (y,m,d,rn,ssn,gton,gtoff)
                f.write(data)
            print(t)
hc.close()
f.close()
########################################################





