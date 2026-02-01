from random import randint

from Oct29_1_OOP.p01_is_a import Product


def printRule(handTable):
    for i, v in enumerate(handTable):   # i는 index로 위치번호 / v는 value로 데이터값? /fruit("apple", "banana", "kiwi") apple i는 0 
        if i != 0:
            print("%d. %s" % (i, v))
            
print("---------------------------------------------------")
def userFire():
    userHand = int(input("뭐냄 : "))
    if 0 < userHand < 4:
        return userHand
    return userFire()

def comFire():
    return randint(1, 3)
##################반복되게################## 
def printHand(handTable, comHand, userHand):
    print("컴 : %s" % handTable[comHand])
    print("나 : %s" % handTable[userHand])

def judge(comHand, userHand, win):
    t = userHand - comHand
    if t == 0:
        print('무')
    elif t == -1 or t == 2:
        print("패")
        print("%d연승" % win )
        return False
    else:
        print("승")
        win += 1
    return True

############################################    
handTable = [None, "가위", "바위", "보"]

printRule(handTable)

win = 0
while True:
    userHand = userFire()
    comHand = comFire()
    printHand(handTable, comHand, userHand)
    result = judge(comHand, userHand, win)
    if result == 10:
        print("%d연승" % win)
        break
    win += result
    print('---------------------')
