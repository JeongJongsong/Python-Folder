
from datetime import datetime
from oracledb import connect


f = open("C:/Users/soldesk/Desktop/jeongjs/seoulDust.csv", "a", encoding="utf-8")

con = connect("js/1234@195.168.9.58:1521/xe")

sql = "select * from seoul_dust"

cur = con.cursor()
cur.execute(sql)
for date, msrrgn_nm, msrste_nm, pm10, pm25, idex_nm in cur:
    date = datetime.strftime(date, "%Y,%m,%d,%H,%M")
    data = "%s,%s,%s,%d,%d,%s\n" % (date, msrrgn_nm, msrste_nm, pm10, pm25, idex_nm)
    f.write(data)

cur.close()
con.close()

f.close()