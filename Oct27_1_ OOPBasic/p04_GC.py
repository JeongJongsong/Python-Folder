# Garbage Collection? -> heap영역 자동정리 시스템
#  자동정리 발동 시점 : 그 번지를 가리키는 변수가 없게 되면

# 어쨌든 Python프로그램은 프로그램 종료시 정리는 다됨
# But 빅데이터를 다뤄야해서 -> 정리를 빨리 해 줄 필요가 있음

###################################################################
# RAM : 변수형태로 임시저장공간(컴 끄면 삭제)
#   OS가 논리적인 3가지 공간으로 나눠 사용
#   static
#   stack : 용량 작은게 저장, 규칙적인 용량이 저장
#           -> 밑에서 부터 차례차례 공간 사용
#           프로그램 종료시 정리됨(없어짐)
#   heap : 용량큰게 저장, 사이즈가 다 천차만별
#           -> 컴이 적당하다 싶은 공간 사용
#           자동정리x, 개발자가 정리해야함

# 이름이 홍길동, 나이가 20살인 학생
# 정보 출력

# 이름이 김길동, 나이가 22살인 학생
# 정보 출력
###################################
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("학생 없어짐")

    def printInfoo(self):
        print(self.name, self.age)
        print("---------------------")

################################
s1 = Student("홍길동", 22)
s1.printInfoo()

s2 = Student("김길동", 26)
s2.printInfoo()

# 연산자 : stack영역대상

#공교롭게도 s1랑 이름이 같고, 나이가 같은 세번째 학생
s3 = s1 #s1 학생을 s3으로도 부를수 있게 함
s3.printInfoo()

#s가 이름을 홍박사로 개명
s1.name = "홍박사"
s1.printInfoo()

s3.printInfoo()
s1 = None
s3 = None
print("ㅋㅋㅋㅋㅋㅋ")