# c8a9fc08a095d7b29d0b8b95b9b848c0 (카카오 REST API키)
# https://dapi.kakao.com/v2/search/blog

from http.client import HTTPSConnection
from json import loads
from urllib.parse import quote
from jeong.jeongStringCleaner import jeongStringCleaner

k = {"Authorization" : "KakaoAK c8a9fc08a095d7b29d0b8b95b9b848c0"}
q = "대만여행"
q = quote(q) #URL인코딩 해주는것
hc = HTTPSConnection("dapi.kakao.com")
hc.request("GET", "/v2/search/blog?query=" + q, headers=k)
resBody = hc.getresponse().read()
print(resBody.decode())
hc.close()

blogData = loads(resBody)
for b in blogData["documents"]:
    print(jeongStringCleaner.clean(b["blogname"]))
    print(jeongStringCleaner.clean(b["title"]))
    print(jeongStringCleaner.clean(b["contents"]))


# blogname, title, contents
