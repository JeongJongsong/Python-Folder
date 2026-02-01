# OOD(Object-Oriented Design)
#   객체지향 프로그래밍 스타일 설계
# 1) OOP : 프로그램 소스로 Ptyhon소스로 리얼월드 묘사하자
#       -> 비만센터에 가서 실제로 비만도 검사하는 장면을 떠올리자
# 2) 만들 프로그램에 필요한것만 남겨서 객체로 표현할 준비
#   ->의사, 손님
# 3) 각 객체의 속성(필요한것만)
# 4) 그 장면 재생 -> 각 객체들의 액션이 있겠쥐??
# 5) 만들거 가기

#   번수
#   전역변수 : 
#   지역변수 : 그 행동하는 동안만 필요함(쓰고 버려)
#   파라메터 : 그 행동하는데 필요한 재료(의사한태 붙어있는거 말고)
#   멤버변수 : 객체의 속성
class Doctor:
    def start(self):
        guest = self.callGuest() # 업무 보는 동안만 의미 있는 손님 -> 지역변수로 처리함
        self.ask(guest) # -> 객체가 메서드(27번줄 ask의 guset(매개변수)) 호출하는거 
        self.calculate(guest)
        self.tellResult(guest)
        
    def callGuest(self):
                # return 이 행동하고나서 생기는 결과물
        return Guest() # 손님 부르고 나면 -> 손님이 생김

    def ask(self, guest):
        guest.tell()

    def calculate(self, guest):
        if guest.height > 3:
            guest.height /= 100
        guest.bmi = guest.weight / (guest.height * guest.height)

        if guest.bmi >= 39:
            guest.result = "고도비만"
        elif guest.bmi >= 32:
            guest.result = "중도비만"
        elif guest.bmi >= 30:
            guest.result = "경도비만"
        elif guest.bmi >= 24:
            guest.result = "과체중"
        elif guest.bmi >= 10:
            guest.result = "정상체중"

    def tellResult(self, guest):
        print("BMI : %.2f" % guest.bmi)
        print("%s님은 %s" % (guest.name, guest.result))
        
# 각 변수 = 지역변수?? 아니고 멤버변수(객체속성)
class Guest:
    def tell(self):
        self.name = input("이름 : ")
        self.height = float(input("키(m) : "))
        self.weight = float(input("몸무게 : "))
    
##################################################
d = Doctor()
d.start()
