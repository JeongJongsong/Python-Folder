from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

from oracledb import connect

hc = HTTPConnection("openapi.seoul.go.kr:8088")
hc.request("GET", "/575a4655496b636839386f58586542/xml/RealtimeCityAir/1/25/")
res = hc.getresponse()
resBody = res.read()
hc.close()
#########################################################
con = connect("js/1234@195.168.9.192:1521/xe")

seoluDustDataa = fromstring(resBody) # xml파싱시작
rowsss = seoluDustDataa.iter("row") # <row></row>들 / iter -> 여러개 찾을때 사용
for r in rowsss:
    msrrgn_nm = r.find("SAREA_NM").text     # <MSRRGN_NM></MSRRGN_NM>    / find -> 하나 찾을때 사용
    msrste_nm = r.find("MSRSTN_NM").text
    pm10 = r.find("PM").text
    pm25 = r.find("FPM").text
    index_nm = r.find("CAI_GRD").text

    sql = "insert into seoul_dust "
    sql += "values(sysdate, '%s', '%s', "% (msrrgn_nm, msrste_nm)
    sql += "%s, %s, '%s')" %(pm10, pm25, index_nm)

    cur = con.cursor() # DB작업 총괄 매니저(1회용)
    cur.execute(sql)
    con.commit()
    cur.close()

con.close()

