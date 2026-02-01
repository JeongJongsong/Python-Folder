from random import randint
from turtle import Turtle


class Refree:
    def __init__(self): # 생성자 만들어서
        self.ruleBook = [None, "가위", "바위", "보"] 

    def blueFire(self, blue):
        return blue.fire()
    
    def callBlueCorner(self):
        return Friend()

    def callRedCorner(self):
        return Player()
    
    def judge(self, bluePaper, redPaper):
        r = redPaper - bluePaper #-> 게임할동안만 필요한 값이라 지역변수로 설정
        if r == 0:
            print("무")
            return 0
        elif r == -1 or r == 2:
            print("패")
            return -999
        else:
            print("승")
            return 1
        
    def redFire(self, red):
        redTemp = red.fire()
        if 0 < redTemp < 4:
            return redTemp
        return self.redFire(red)
    
    def tellHand(self, bluePaper, redPaper):
        print("컴 : %s" % self.ruleBook[bluePaper])
        print("나 : %s" % self.ruleBook[redPaper])

    def tellResult(self, win):
        print("%d연승" % win)


    def tellRule(self):
        for i, v in enumerate(self.ruleBook):
            if i != 0:
                print("%d. %s" % (i, v))
            # print("가위") 유지보수 측면에선 이렇게 하는게 나음
            # print("바위") 
            # print("보") 
    
        print("----------------------------------------------------")
        
    def start(self):
        blue = self.callBlueCorner() #게임하는 동안만 필요함 -> 지역변수
        red = self.callRedCorner() #게임하는 동안만 필요함 -> 지역변수
        self.tellRule()
        win = 0
        while True:
            bluePaper = self.blueFire(blue)
            redPaper = self.redFire(red)
            self.tellHand(bluePaper, redPaper)
            r = self.judge(bluePaper, redPaper)
            if r == -999:
                break
            win += r
            print("-----------------")
        self.tellResult(win)


class Friend:
    def fire(self):
        return randint(1, 3)

class Player:
    def fire(self):
        return int(input("뭐낼껴? : "))

################################
r = Refree()
r.start()