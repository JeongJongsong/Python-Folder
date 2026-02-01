#  PL 어려운가? -> ㅇㅇ 어려움
#   왜어려움? -> 일상 언어랑 생긴게 너무 다르름
#   how to easy? 그럼 일상 언어랑 비슷하게 되면 쉬워지겠쥥?

# 효율적이 프로그램 만들자
# 요즘 컴 H/W 사양이 줜나 좋아져서 -> 효율성이 그닥 안중요해짐
# 아고리즘의 시대 -> 유지보수의 시대
# 좋은 알고리즘 보다는 유지보수하기좋게 만들자 -> 이게 더 중요해짐
# 유지보수하기 좋으려면 -> 소스가 알아보기 편해야함 -> 알아보기 편하려면 일상언어처럼...
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# PP(Procedural Programming) : 절차지향 프로그래밍
#   함수, 조건문, ....... 순서대로 잘 써서 프로그램 만들자

# OOP(Object-Oriented Programming) : 객체지향프로그래밍
#   프로그램 소스를 일상언어스럽게 쓰자
#   객체라는걸 써서 realWorld를 묘사하자
#   객체 : 실생활에 존재하는 어떤 존재(실존안하는 추상적인 개념일수도)
#   객체를 만드려면 클래스class가 필요함

# function vs method
# function : 기능 모아 놓은것
# method : class의 member함수? 정도로 받아 들이면 됨
#           객체의 액션


# 변수
#   전역변수(global variable) : 그냥 밖에있는 변수
#       global만 붙이면 어디서든 사용가능
#   지역변수(local variable) : 함수/메소드 속에서 만든거
#       함수/메소드 속에서만 사용 가능
#       함수/메소드 진행하는 동안만 쓰고 버릴것(임시사용)
#   맴버변수(member variable)
#       member variable, attribute, field
#       객체의 속성


# class : 객체 찍어낼때 쓰는 도장/붕어빵틀 같은거
from os import name
class dog:
    name = None # member variable : 객체의 속성 -> class 안에 넣는것들은 member
    age = None

    def bark(self):# method : 객체의 액션   ()안에 첫번째로 무조건 self 들어가야함
        print("멍멍멍멍왈왈왈크르르을으!!")

    def showDogInfo(self):    # method : 프로그램상 필요한 기능
        print(self.name) # 이 개의 name -> d.name인지 d2.name지 모르니까
        print(self.age)
###############
# object/instance : 그 틀을 가지고 찍어낸 붕어빵
d = dog()       # 개를 하나 만들어서 d라는 변수에 저장
d.name = "후추" # d의 이름이 후추
d.age = 3       # d 의 나이가 3살
d.bark()        # d가 짖음
d.showDogInfo()

print("---------------------------------------------")

d2 = dog()
d2.name = "왈왈이"
d2.age = 2
d2.bark()
d2.showDogInfo()

# 개 이름 후추

# 나이 3살

# 그 개가 짖어 : 멍 출력


# from traceback import print_tb
# dogName = "후추"
# dogAge = "3살"
# dogSound = "멍멍멍왈왈왈"

# print("개이름은 %s이고, 나이는 %s 입니다." %(dogName, dogAge))
# print("짖어!!", dogSound)
