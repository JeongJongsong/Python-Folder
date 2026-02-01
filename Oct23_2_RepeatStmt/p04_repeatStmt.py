# 1 + 2 + 3 + 4 .... + 20 = ?
from random import randint


a = 0
for i in range(1,21):
    a += i
print(a)
print("----------------------------------")
# 1 + 2+ 3 +........ + ? > 100 / 100넘기는 ?의 최소값 구해라

          
# 반복문
#   컬렉션 탐색용 : for 문
#   반복횟수 : for에 range활용해서 사용
#   반복조건 : while
#       while 조건식:
#           조건식 만족되면 실행 반복

# 랜덤
b = randint(1, 10) # 1 ~ 5 사이의 랜덤한 정수
print(b)
print("----------------------------------")

# 1 ~ 10 사시의 랜덤한 정수
# 10번 출력하기
for i in range(10):
    c = randint(1, 10)
    print(c)
print("---------------------------------------")

# 1 ~10사이의 랜덤한 정수 4나올때 까지 출력시키기
d = randint(1, 10)
print(d)
while d != 4:
    d = randint(1, 10)
    print(d)
print("---------------------------------------")

# 정수하나 입력 받아서 출력하는데 5라고 쓸때까지
e = int(input("숫자입력해 : "))
print(e)
while e != 5:
    e = int(input("숫자입력해 : "))
    print(e)