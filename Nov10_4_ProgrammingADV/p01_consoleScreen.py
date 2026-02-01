# 일단 회사등록 시켜야함
# 1 회사 데이터 확보해야겠쥐?
# 그럼 input으로 값받을수 있게 해
# 객체를 만들어야지?
#  front-end 부분
from p01_company import Company

class ConsoleScreen:
    def getInfo():
        name = input("회사 이름 : ")
        boss = input("사장이름 : ")
        head = input("회사주소 : ")
        empployee = input("직원 수 : ")
        return Company(name, boss, head, empployee)
    
    def printResult(result):
        print(result)
    