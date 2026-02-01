# 함수
#   정리차원
#   속도 느려짐(점프연산)
#   -> recursiveCall : 계산용x
#       계산문제는 반복문

from time import sleep


def getEven(): #짝수 입력 받는 함수
    num = int(input("숫자를 입력하세요 : ")) # 사용자로부터 숫자 하나 받음
    if num % 2 == 0: # 짝수면
        return num # 받은 숫자를 결과로 줘
    else: #그 숫자가 홀수면
        print("짝수를 입력하세요.")
        sleep(2)
        return getEven()

# num = int(input("숫자를 입력하세요 : "))
num = getEven() # 위에 줄이 최종적으로 이렇게 된거임
                # 짝수로 값을 받는 소스가 getEven()함수에 다 있음
print("입력한 숫자는 %d 입니다." %num)

