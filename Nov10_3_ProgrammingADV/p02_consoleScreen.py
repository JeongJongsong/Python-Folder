from p02_guset import Guest
# 여기서는 사용자한태 입력 받는 부분탈모
class ConsoleScreen:
    def getGuestInfo():
        name = input("이름 : ")
        height = input("키(m) : ")
        weight = input("몸무게 : ")
        return Guest(name, height, weight)

    def printResult(guest):
        print("BMI : %.2f" % guest.bmi)
        print("%s님은 %s" % (guest.name, guest.result))