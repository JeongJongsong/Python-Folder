# OOP 객체지향 스타일로 나눈 결과 구해서 출력
# z = ???
# 출력
class Calculator:
    def getMoks(x,y):
        try:
            z = x / y
            return z
        except:
            print("나누기 0은 없다 이자시가")
            return -999 #
        finally:
            print("어쨌든 계산 끝남 어쩔래미")
    
############################################
x = int(input("x : "))
y = int(input("y : "))

z = Calculator.getMoks(x, y)
print(z)    


        
    
