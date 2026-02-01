# 객체간의 관계
# has a
#  is a
# 상속


from tkinter.ttk import Notebook


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def showInfo(self):
        print(self.name, self.price)
# 우리 쇼핑몰의 모든 상품들은 상품명/가격 다있음
# Pen은 상품명/가격에 "색깔"이 추가됨 

# 상속 = 기능확장

# Pen is a Product --> OOP의 상속 사용 가능
#   Product에 있는 멤버들(멤버번수, 메소드)이 Pen쪽 으로 상속됨
# Product로 부터 상속받는 Pen
# Product : 상위/부모/super 클래스
# Pen : 하위/자식클래스

#예제 1)
class Pen(Product):
    def __init__(self, name, price):
        super().__init__(name, price)

# 우유부터 유통기한 -> 기능 확장(상속)
#   대부분 PL은 생성자는 상속 안시켜줌
#   Python은 보통 생성자에서 멤버변수를 결정
#       -> 생성자를 상속 안시켜? -> 멤버변수도 상속 안시켜?
#       => 생성자도 상속됨
# self : 지금 이 클래스를 지칭함
# super : 상위클래스를 지칭함

# 예제 2)
class Milk(Product):
    # 상속받은게 아니고 새로 만든거 -> 생성자 상속이 의미가 있나???...
    # overridng : 상속(확장)받아온 생성자 기능 바꾸기 -> overriding이라 부르기는 애매
    # overloading : 똑같은 이름 메소드 여러개 -> overloading이라 부르기도 애매
    def __init__(self, name, price, exp): 
        super().__init__(name, price) #Product클래스에 있는 생성자 부른거 -> 이름, 가격 세팅됨
        self.exp = exp

    # 정보 출력할때 유통기한도 출력하고 싶음
    # Product로 부터 상속받아온 showInfo는 이름/가격만 출력
    # overriding : 상속(확장)받아온 메소드(showInfo)의 기능 개조
    def showInfo(self):
        super().showInfo() # Product에 있는 showInfo호출 -> 이름/가격/ 출력
        print(self.exp)
#예제 3)
class Shose(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def showInfo(self):
        super().showInfo()
        print(self.size)

print("-----------------")

#예제 4)
class Computer(Product):
    def __init__(self, name, price, cpu, ram, Hdd):
        super().__init__(name, price)
        self.cpu = cpu
        self.ram = ram
        self.Hdd = Hdd
    def showInfo(self):
        super().showInfo()
        print(self.cpu, self.ram, self.Hdd)

#예제 5)
#-> 다단상속 
class Notebook(Computer):
    def __init__(self, name, price, cpu, ram, Hdd, weight):
        super().__init__(name, price, cpu, ram, Hdd)
        self.weight = weight
    def showInfo(self):
        super().showInfo() # 여기서 super(상위클라스)는 Computer
        print(self.weight)
#############################
# 품명이 모나미153, 가격이 500원 상품 -> 정보출력
p = Pen("모나미153", 500)
p.showInfo()

# 품명이 서울우유1L, 가격이 3000원 우유 
m = Milk("서울우유1L", 3000, "2025.11.09")
m.showInfo()

# 품명이 조던123, 150000, 270사이즈 신발 출력
s = Shose("조던123", 150000, "270")
s.showInfo()

# 품명 매직스테이션123, 200000, i7-1234, 램32, Hdd 500 컴퓨터 -> 정보출력
c = Computer("매직스테이션123", 200000, "i7-1234", "32", "500")
c.showInfo()
    
# 품명 그램123, 2500000, i7-5678, 램32, Hdd 1000 3kg 노트북 -> 정보출력
n = Notebook("그램123", 2500000, "i7-5678", "32", "1000", "3")
n.showInfo()

print("-----------------------------")

