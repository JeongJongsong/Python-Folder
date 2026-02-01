# 생년월일(yyyy/mm/dd) : 입력받아
# 받은 생년월일의 요일: 나이(한국나이)
from datetime import datetime

# 나이는 지금년도 - 입력받은 년도 +1
birthday = input("생년월일(yyyy/mm/dd) : ")
print("---------------------------------")
# 내가 한부분 ------------------
# birthday = birthday.split("/")
# y = int(birthday[0])
# m = int(birthday[1])
# d = int(birthday[2])

now = datetime.today()
curYear = now.year
birthYear = int(birthday[0:4])
age = (curYear - birthYear) + 1
print("올해는 %d년 입니다." % curYear)
print("나이 : %d세 입니다." % age)
# 요일 : 어캄 ㅠㅠ
birthday2 = datetime.strptime(birthday, "%Y/%m/%d")
yoil = datetime.strftime(birthday2, "%A")
print("요일 : %s" % yoil)