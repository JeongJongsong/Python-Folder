# 1) 컴이 1~1만 사이 랜덤한 숫자 하나 뽑고 
from random import randint

turn = 0
###############################################
def getUserAns():
    userAns = int(input("무슨 숫자 일까요? :"))
    if 0 < userAns < 10001:
        return userAns
    return getUserAns()

def getGameAns():
    return randint(1, 10001)

######################################
# 판정하고나서, 게임 계속해야하는지 여부 리턴되는 함수
def judge(gameAns, userAns):
    global turn
    if  gameAns == userAns:
        print("%d턴만에 정답" % turn)
        return False
    elif gameAns > userAns:
        print("up")
    else:
        print("down")
    return True
#########################################################-
gameAns = getGameAns()
print(gameAns)

while True:
    turn += 1
    userAns = getUserAns()
    go = judge(gameAns, userAns)
    if not go :
        break
# 맞출때까지 반복하고
# -----------------------------------------------------
# 정답 맞추면
# 몇번만에 정답 맞춤 출력되게




