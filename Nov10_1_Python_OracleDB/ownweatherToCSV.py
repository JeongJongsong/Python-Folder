from datetime import datetime
from oracledb import connect


f = open("C:/Users/soldesk/Desktop/jeongjs/openWeather.csv", "a", encoding="utf-8")

con = connect("js/1234@195.168.9.58:1521/xe")

sql = "select * from own_weather"

cur = con.cursor()
cur.execute(sql)
for date, desc, temp, humi in cur:
    date = datetime.strftime(date, "%Y,%m,%d,%H,%M")
    data = "%s,%s,%.2f,%d\n" % (date, desc, temp, humi)
    f.write(data)

cur.close()
con.close()

f.close()
