# 프로그래밍 언어에 어떠한 기능이 어떠한 시기에 만들어 짐
# 세월이 가고, 기술 발전하면 그 시점에 만들어진 그 기능을 못쓰게됨
# -> 그 기능 고쳐야함


# deprecated
#   그 기능 업그레이드or 삭제 or ....할 예정
# 그래서 뭐할땐 어쩌고 뭐할땐 저쩌고 이런거 외우지 마라
#   유예기간이라고 생각하면됨
#       현재버전에서는 작동하는데
#       다음버전에서는 없어져도 이상할게 없음
#   ->그래서 안쓰는 쪽으로 가는게 좋음 -> 그래서 이러한 변화에 민감해져야함(이게 트랜드)

# 면접 기출 문제 deprecated 가 뭔지 설명해라

# 패키지명 : x
# 모듈명 : datetime.py
# 클래스명 : datetime
# today()의 정체 : static 메소드

from datetime import datetime
from time import strftime

now = datetime.today() # 자동으로 현재시간날짜 
print(now)
print(now.year) #연도만
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

# 특정시간날짜 보고 싶으면
d = datetime(1994, 6, 7) #객체지향으로 객체만들어서 

# d2 = input("날짜(yyyy/mm/dd) : ") # 날짜(yyyy/mm/dd) 입력 받아서
# d2 = d2.split("/") # datetime 객체로 
# y = int(d2[0])
# m = int(d2[1])
# d = int(d2[2])  -> d2[2]는 str이라 int로 바꿔준거
# d2 = datetime(y, m, d)
# print(d2)

# 패턴알고싶으면 
# help(strftime)

# str -> datetime 으로 바꾸려면
d3 = "2002/06/07"
d3 = datetime.strptime(d3, "%Y/%m/%d")
print(d3)

d4 = datetime.today()
y = d4.year
m = d4.month
d = d4.day
h = d4.hour
mi = d4.minute
print("%d.%d.%d %d:%d" % (y, m, d, h, mi))
# 2025.10.30 15:53 이런 형태로 나오게 출력시켜봐봐

# datetime -> str
d5 = datetime.today()
d5 = datetime.strftime(d5, "%Y.%m.%d %H:%M:%S")
print(d5)