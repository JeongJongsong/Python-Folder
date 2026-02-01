# 숫자 1개 넣으면, 홀수인지 아닌지 출력해주는 함수
from time import sleep

# 만든 그 함수 써서 13 홀수인지
def printHolNum(a):
    print(a % 2 == 1)

# 숫자 1개 넣으면, 홀수인지 아닌지 구해주는 함수
def getIsodd(a):
    odd = a % 2 == 1  # 구하기는 했는데 odd 값을 함수밖에 있는 값 어떻게 씀
    return odd

# 숫자 1개 넣으면, 2배한값 구해주는 함수
def getDouble(a):
    double = a * 2
    return double

# 숫자 4개 리턴 불가
# list, set, dict, tuple....등등 1개 리턴가능
# 숫자 2개 넣으면, 사칙연산결과를 구해주는 함수
def calculate(x, y):
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    return a, b, c, d #tuple 1개 리턴시킨거임 -> tuple이라 () 생략된것

#################################
printHolNum(13)
printHolNum(14)

double = getDouble(5)
sleep(double)  # 프로그램 진행을()값 만큼 멈췄다가 실행 ->여기서는 (10)이니까 10초 멈추고 실행함

odd = getIsodd(10)
print(odd)

# 그 함수 써서 1,4의 합 구해서
# 그만큼 멈췄다가 실행되게
aaa, bbb, _, ddd = calculate(10, 5) # -> _이거 쓰면 값 필요없는 값 뺌
print(aaa)
print(bbb)

e = calculate(10, 5)
print(e, type(e))
