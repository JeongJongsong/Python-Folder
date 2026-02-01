# https://api.openweathermap.org/data/2.5/weather?q=pairs&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr

from http.client import HTTPConnection
from json import loads
from oracledb import connect

#########下面的文法就是鏈接HTTP通訊的###########
hc = HTTPConnection("api.openweathermap.org")
hc.request("GET", "/data/2.5/weather?q=seoul&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr")
resBody = hc.getresponse().read()
hc.close()
################################
con = connect("js/1234@195.168.9.192:1521/xe")

weatherData = loads(resBody) #json 파싱 함
description = (weatherData["weather"][0]["description"])
temp = (weatherData["main"]["temp"])
humidity = (weatherData["main"]["humidity"])


sql = "insert into own_weather "
sql += "values(sysdate, '%s', '%s', '%s')" %(description, temp, humidity)

cur = con.cursor()
cur.execute(sql)
con.commit()

cur.close()
con.close()
