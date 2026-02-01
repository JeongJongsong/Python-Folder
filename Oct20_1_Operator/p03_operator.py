# 연산자 
#   다른 언어들은 Stack 영역이 대상
#   Python은 모든 데이터가 다 heap영역
#       -> 연산자 써놓으면 대충 알아들음

# 에버랜드 놀이기구 탑승 제한 만들기
# 키, 나이 정보 입력 받고 출력하기
name = str(input("이름 : ")) #str 글자
height = float(input("키 : ")) #float 실수(소숫점)
age = int(input("나이 : ")) #int(정수)
print("------------------")
print("키는 : %.1fcm, 나이는 : %d살" % (height, age))

# 논리연산자(Bool) : 결과로 True/False
# 초과 이상 같다 다르다 이하 미만 
# >    >=   ==    !=    <=   <    
# -------------------------------------------------------

# a는 키가 130 초과 탑승 가능
a = (height > 130)
print(a)
# b는 나이가 10살 미만 탑승 가능
b = (age < 10)
print(b)
# C는 키 120 이하 탑승가능
c = (height <= 120)
print(c)
# d는 나이가 5살 탑승가능
d = (age == 5)
print(d)
# e는 나이가 10살만 못탐
e = (age != 10)
print(e) 
# f는 나이가 홀수여야 탑승가능
f = (age % 2 == 1)
print(f)
# g는 이름이 홍길동이어야 탐
g = (name == "홍길동")
print(g)

# =======================================================
#           그리고(and) 또는(or) 반대(not)  xor
# 다른언어       &&, &    ||,|       !       ^
# Python         and, &   or, |      not     ^

# and                               or 
# A B                               A B
# o o -> o                          o o -> o
# o x -> x                          o x -> o
# x o -> x                          x o -> o
# x x -> x                          x x -> x

# h는 키가 100이상이고, 나이 80살 이상 and
h = (height >= 100) and (age >= 80) # 검사 3번해야함 100 -> and -> 80
h = (age >= 8) and (height >= 100) # 검사 2번만에 끝남
print(h)
# -> 순서에 따라 검사 횟수(속도)달라짐 / and로 묶을 때는 희귀한거 앞에

# i는 나이가 90이상이거나, 키가 80이상 탑승가능  or
i = (age >= 90) or (height >= 80) 
i = (height >= 80) or (age >= 90)
print(i)  
# -> 순서에 따라 검사 횟수(속도)달라짐 / or로 묶을 떄는 일반적인걸 앞에

# -----------------------------------------------------------------------
# XOR(eXclusive OR - 배타적 OR)
#   a b
#   o o -> x
#   o x -> o
#   x o -> o
#   x x -> x

print(i)
# j는 i의 반대
j = not i
print(j)

# k는 나이가 100살 이상이든지, 키가 100이상 이든지 둘중 하나만
k = (height >= 100) ^ (age >= 100) 
print(k)

# l은 나이가 20살 미만이든지, 나이가 80살 초과하든지
l = (age < 20) or (age > 80) #or은 일반적인걸 앞으로
print(l)

# m은 10 <= 나이 <= 30
m = (10 <= age <= 30) #Python은 이렇게 가능
m = (age >= 10) and (age <= 30) #다른언어에서는 이렇게 풀어써야됨
#and는 비교적 희귀한걸 앞에
print(m)

# n은 나이가 10살 넘고, 나이가 50살 넘고
# n = (age > 10) and (age > 50)
n = (age > 50)
print(n)

# 단항연산 : not
# 2항연산 : 대부분
# 3항연산
#   조건 따져서 변수값 넣을 때
#   조건식: 조건 ? 참일떄 값 : 거짓일때 값 -> Python에는 없음