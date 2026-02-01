# 1) 실생활에 존재하는 고양이 표현하자
# 3) 객체를 만드려면 클래스가 필요하다
class Cat:
    # name = "나비" # 객체의 속성 : 전세계의 모든 고양이 이름이 나비???
    # 어차피 외부에서 추가 가능 -> 이렇게 잘 안씀
    name = None #    # 어차피 외부에서 추가 가능 -> 이렇게 잘 안씀
    age = None  # ->여기에 값 넣으면 이상해짐

    #객체의 액션/프로그램의 기능
    def meow(self, cnt): # 메소드 첫번째 파라메터는 self, 두번째 부터는 맘대로
        print("냥" * cnt)

    def showww(self):
        print(self.name)
        print(self.age)

###############
# 2) 고양이 객체 만들자
c = Cat()

# 멤버변수 접근 : 변수명.멤버변수명
c.name = "나비"
c.age = 1
c.weight = 3 # Python은 클래스 외부에서 속성 추가 가능 -> 파이썬만 가능

# 메소드 호출 : 
# 원래 Python의 메소드 호출은 : class명. 메소드명(변수명, ...)
Cat.meow(c, 5)


# Python이 버전업되다가, 다른PL처럼 허용해준 문법 : 변수명.메소드명(...)
c.meow(5) #호출할때 self는 없는셈 침

Cat.showww(c)
c.showww()
# 두개 똑같으니 둘중 맘에 드는걸로 하면됨 


print(c.name)
print(c.age)
print(c.weight)

