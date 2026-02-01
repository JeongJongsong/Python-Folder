# 프로그래밍 패러다임
# PP(Procedural Programming)
#   절차지향프로그래밍
#   순서대로 잘 써서 결과 잘 내자
#=========================================
# OOP(Object Oriented Programming)
#   객체지향프로그래밍
#   실생활을 묘사해서, 유지보수하기 좋게 하

#=========================================
# AOP(Aspect Oriented Programming)
#   관점지향프로그래밍
#   OOP를 다른 관점에서 보자

#=========================================
#  사람객체 하나 만들기

##########################
class human :
    def __init__(self, name, age):
        self.name =name
        self.age = age
            
    def printinfo(self):
        print(self.name, self.age)
    
    # 학교가기, 공원가기, 마트가기, 공통된 부분
    # 나갈준비하기라는 메소드로 따로 정리
    def ready(self):
        print("씻고 나갈준비")
        print("엘배타고 1층으로")

    def goAcademy(self):
        self.ready()
        print("버스타고 학원으로로")
    
    def goLotteworld(self):
        self.ready()
        print("걸어서 롯데월드로")

    def goEmart(self):
        self.ready()
        print("걸어서 마트로")

    def goPark(self):
        self.ready()
        print("앱켜고 어캐가는지 확인하고 공원으로")
        
##########################
h = human("홍길동", 30)
h.printinfo()
h.goAcademy
h.goLotteworld
h.goEmart
h.goPark

# 학원가기
# 마트가기
# 공원가기  기능 추가