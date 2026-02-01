# constructor(생성자) : 객체가 만들어질때 호출되는 메소드
# destructor(소멸자) : 객체가 사라질때 호출되는 메소드



################################################
# 이름이 모나미153, 색깔이 검정, 가격이 500원인 펜 정보출력
class ballpen:
    # 여기다 멤버변수 써놓는게 별 의미없음(어차피 외부에서 추가가능)
    # name = None
    # color = None
    # pirce = None

    # 다른 PL들이 많이들 활용하는 생성자 overlading이 Python은 불가
    # -> 무조건 생성자는 하나만 존재가능
    # => Python개발자들이 멤버변수를 생성자에서 결정하는 문화
    def __init__(self, name, color, price): # 멤버변수를 생성자()안 에서 결정함
        self.name = name
        self.color = color
        self.pirce = price


    def showw(self):
        print(self.name, self.color, self.pirce)

################################################
#제목이 점프투파이썬, 가격이20000원인 책
# 정보출력

class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price
    def printtt(self):
        print(self.title, self.price)
#################################################
b = Book("점프투파이썬", 20000)
b.printtt()


################################################
p = ballpen("모나미153", "검정", 500)
p.showw()




################################################
#컴퓨터 만들어
# cpu가 i9-1234
# Ram이 64
# hdd 500
# 정보출력

class Computer:
    cpu = None
    Ram = None
    hdd = None
    # 컴이 만들어 질때 뭔가 하고싶어서 ->생성자 만듦
    # 뭐하게 : 아예 컴 만들면서 cpu/ram/hdd 값 넣게
    def __init__(self, cpu, Ram, hdd):
        self.cpu = cpu
        self.Ram = Ram
        self.hdd = hdd

    def showInfoo(self):
        print(self.cpu, self.Ram, self.hdd)
###################################

c = Computer("i9-1234", 64, 500)
c.cpu = "i9-1234"
c.Ram = 64
c.hdd = 500
#Computer.showInfoo
c.showInfoo()




################################################
# 객체 생성
# 변수명 = 클래스명() -> 생성자 호출하는거
# 핸드폰
# 모델명 ->
# 번호 ->
# 가격 ->
# 정보출력
class Handphone:
    model = None
    num = None
    price = None

    # default constructor(기본생성자)
    # 생성자 작업을 전혀 하지 않으면
    # Python이 내부적으로 만들어서 사용
    def __init__(self): #생성자
        print("핸드폰 생성")

    def __del__(self): # 소멸자
        print("핸드폰 사라짐")

    def printInfo(self):
        print(self.model, self.num, self.price)


h = Handphone()
h.model = "갤럭시 Z 플립 7"
h.num = "010-0000-1234"
h.price = 1200000

# Handphone.printInfo(h) #->원래 파이썬 스타일
h.printInfo() # -> 다른언어랑 같은 스타일