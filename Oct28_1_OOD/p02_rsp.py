#가위바위보 객체지향으로 만들어보기


# computer , user 객체 2개 있어야함
# 
# 컴터가 필요한것 
# 1. 가위바위보 리스트
# 2. 랜덤으로 가위바위보 선택 -> 이건 게임중에만 쓰니깐 지역변수로 처리해
# 3. 유저가 낸것

# 판단매소드(유저입장에서)
# 컴꺼랑 유저꺼랑 비교
# 만약 같으면 무 출력
# elif 컴터꺼 > 유저꺼 패 출력 
# 패 할땐 여기서 종료시키고 몇연승 했는지 출력시켜
# else 승 출력 
# 승 일때 win 1씩 증가 시키고 계속진행

# 유저가 필요한것
# 1. 가위바위보 리스트
# 2. 가위바위보 입력하는 도구 (가위바위보 중 하나 입력받기)

# 가위바위를 리스트화해서 


# 밑에껀 내가 끄적거린건데 거의 배끼다싶이 한거 주륵
from random import randint



class Computer:

    def comHand(self):
        return randint(1, 3) #컴터가 랜덤으로 가위바위보 선택하는거
    
    def start(self, user):
        win = 0 #게임 하는 동안만 의미있는거 -> 지역변수로 처리
        comAns = self.comHand()
        print(comAns)
        while True:
            win += 1
            userAns = self.ask(user)
            if not self. judge(comAns, userAns):
                break

    def ask(self, user):
        userHand = user.tell()
        if 0 < userHand < 4:
            return userHand
        return self.ask(user)


    def judge(self, comHand, userHand):
        r = userHand - comHand
        if r == 0:
            print("무")
        elif r == -1 or r == 2:
            print("패")
            print("%d연승" % win)
            return False
        else:
            print("승")
        return True
    

class User:
    def tell(self):
        return int(input("뭐냄? : "))



handTable = [None, "가위", "바위", "보"] # ->가위바위보 리스트를 만들어줘
computer = Computer()
user = User()
computer.start(user)
