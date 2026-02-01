# View : 실제로 사용자 눈에 보이는 파일, 
#   실제로 입력받고 결과 출력하는 용도
#   front-end 개발자 + 디자이너 -> Python 개발자는 아님
#-> front-end 개발자 입장에서 작성
class ConsoleScreen: 
    def getXY(): #-> 앞으로는 이부분이 python이 아님 app이나 웹 / 최대한 간단하게 적는 연습 고고
        x = input("x : ")
        y = input("y : ")
        return x, y
    
    def printResult(c):
        print(c)