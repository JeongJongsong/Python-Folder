# 1 -> 가위 
# 2 -> 바위 
# 3 -> 보  출력
#==================
# 뭐내는지 입력 받고
# 컴터 : 가위
# 나 : 바위
# 결과 : 승
# =================
# 뭐내는지 입력 받고
# 컴터 : 보
# 나 : 보
# 결과 : 무승부
#==================
# 뭐내는지 입력 받고
# 컴터 : 보
# 나 : 보
# 결과 : 무승부
# 비기면 무  출력되게
# 몇 연승 중인지 출력되게
# 질때까지 반복

from random import randint

handTable = ["", "가위", "바위", "보"] # list로 만들어
# handTable[2] # -> 이렇게하면 2 = 바위 

for i, v in enumerate(handTable):
    if i != 0:
        print("%d. %s" %(i, v))     # -> 이렇게하면 1.가위 2.바위 3.보 
print("---------------------------------------------------")
win = 0
while True:
    userHand = int(input("뭐냄 : "))
    comHand = randint(1, 3)
    print("컴 : %s" % handTable[comHand])
    print("나 : %s" % handTable[userHand])

    t = userHand - comHand
    if t == 0:
        print("무")
    elif t == -1 or t == 2:
        print("패")
        print("%d연승" %win)
        break
    else:
        print("승")
        win += 1
    print("----------------------------------------------------")










