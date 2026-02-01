# 일반함수
#   소스정리용이    : 만들어 놓고 여러번 사용
#   parameter       : 함수 실행에 필요한 재료 함수명()  ()여기에 들어가는것
#   return          : 함수 결과물 돌려주는 명령어
# lambda 함수       : 이름 없는 1회용 함수
#   언제 왜? -> 값을 간단하게 구할때
#   (lambda parameter변수명, parameter변수명, ....:내용)(값)

(lambda n:print(n))("정종성")

print("-------------------")

# 숫자 3개 넣으면, 그 평균값 구해주는 함수
def getAverage(x, y, z):
    # average = (x + y + z) / 3
    return (x + y + z) / 3
# lambda함수는 애초에 값 구하는 용도라 그냥 값만 써주면 return으로 자동
#---> lambda로 바꾸면
d = (lambda x, y, z:(x+y+z)/3)(10, 20,55)
print(d)

# 자기 이름 출력하는 함수
# 사용
def printName(n): # (lambda n:)
    print(n) # (lambda n:print(n))
printName("정종성") # (lambda n:print(n))("정종성")

# ==========================================================================
# 10, 20, 55 의 평균값 출력
d = getAverage(10, 20, 55)
print(d)
# 556, 100, 2의 평균
d = getAverage(556, 100, 2)
print(d)
# 출력
