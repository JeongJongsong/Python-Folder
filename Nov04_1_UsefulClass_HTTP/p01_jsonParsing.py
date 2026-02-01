# 데이터를 특정형식으로 표현해야
# -> HTML모양으로 하자 ->XML
# XML보다 더 괜찮은거 없을까?
# 그럼 JavaScript모양으로 하자 -> JSON


# JSON(JavaScript Objiect Notation)
#   모든면에서 XML보다 우월 
#       -> 最近大部分使用JSON
#       -> 可讀性은 XML이 더 나음 -> 각종설정파일로 XML사용
#   JS객체
#       {멤버변수(속성)명:값, 멤버변수(속성)명:값, ...} -> Python dict 랑 문법같음
#   JS배열
#       [값, 값, ....] 이런식                           -> Python list와 문법 같음



# https://api.openweathermap.org/data/2.5/weather?q=pairs&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr

from http.client import HTTPConnection
from json import loads

#########下面的文法就是鏈接HTTP通訊的###########
hc = HTTPConnection("api.openweathermap.org")
hc.request("GET", "/data/2.5/weather?q=pairs&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr")
resBody = hc.getresponse().read()
hc.close()
################################
# description
# temp
# humidity 출력해보자
weatherData = loads(resBody) # -> JSON 파싱은 이 loads()로 시작
print(weatherData["weather"][0]["description"]) # 이게 날씨
print(weatherData["main"]["temp"])
print(weatherData["main"]["humidity"])


