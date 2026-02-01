# 어벤져스
#   이름 
#   나이
#   정보출력기능 -> 본명/나이 출력
#   공격하기기능 -> 공격하기 출력

class Avengers:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def printInfo(self):
        print(self.name, self.age)
    def attack(self):
        print("공격하기")

# 사람 이름, 집주소, 밥먹기기기능 -> 냠 출력
# 정보출력기능 -> 이름/집주소 출력
class Human:
    def __init__(self, name, adress):
        self.name = name
        self.adress = adress

    def eat(self):
        print("냠냠")

    def printInfo(self):
        print(self.name, self.adress)

# Ironman is a Avengers
# Ironman is a Human 
# -> 다중상속(확장) Avengers에도 속하면서 Human에도 속하는것
# PL들 마다 다중상속 지원하냐 마냐 -> 대부분 안됨
# Python은 다중상속 가능
#       다중상속 상황에서 이름이 같으면 어쩔껴?
#       -> 먼저 상속받은걸로 -> 그럼 그 다음 상속받은건 안됨? 
#       -> 그럼 다중상속 왜함?
class IronMan(Avengers, Human):
    def __init__(self, name, age, com, address): 
        #com, address 부분은 사람이 추가 해줘야함
        super().__init__(name, age)
        self.com = com
        self.address = address

    def printInfo(self):
        super().printInfo()
        print(self.com)
        print(self.address)

#########################################
#  이름이 토니, 나이 40, 컴터이름이 자비스인 아이언맨
# 공격하기, 정보출력
i = IronMan("토니", 40, "자비스", "뉴욕")
i.attack()
i.eat()
i.printInfo()