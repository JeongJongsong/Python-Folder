# 대부분 PL -> 기본형, 객체, ...
# Python = 기본형이 없고 전부 다 객체 (특이한 부분탈모임)

# 객체간의 관계
#   Human has a Dog - 키우는 개
#   Dog has a Human - 개 주인
#   Human has a 이름
#   Human has a 나이
############################################
# 이름이 홍길동, 나이가 30살인 사람
# 정보출력

from tkinter.messagebox import showinfo


class Human: #붕어빵틀
    def __init__(self, name, age, pet):
        self.name = name
        self.age = age
        self.pet = pet

    def printInfo(self):
        print(self.name, self.age)
        self.pet.showInfo()
class Dog:
    def __init__(self, name, kind, bug):
        self.name = name
        self.kind = kind
        self.bug = bug
        
    def showInfo(self):
        print(self.name, self.kind)
        self.bug.show()

####################################
# 이름이 벼룩, 크기가 1mm인 벌레
class Bug:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def show(self):
        print(self.name, self.size)

b = Bug("벼룩이", "1mm")
b.show()
# 후추한태 벼룩이 붙어있다
# 후추 정보 찍을때 붙어있는 벌레 정보도 찍고싶다.
print("-----------------------------------")

d = Dog("후추", "말티즈", b)
d.showInfo()

print("-----------------------------------")

h = Human("홍길동", 30, d) # 붕어빵
h.printInfo()

#이름이 후추, 견종이 말티즈인 개
# 정보출력

