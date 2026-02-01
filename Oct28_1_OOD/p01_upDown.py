# static method
#   일반 method : 객체의 액션(객체가 있어야 사용가능)
#   static method : 객체가 없어도 쓸수있는 메소드(함수?)
#################################################
# 변수
#   전역변수 
#   지역변수 : 함수 속에서 만든거 -> 함수 하는 동안만 쓰고 버리는거
#   파라메터 : 함수 진행에 필요한 재료
#   멤버변수 : 객체의 속성
#-----------------------------------------------
# 변수 언제 만드나? - 데이터 임시저장할때
# 객체 언제 만드나? - 실생활스럽게 데이터 임시저장하려고


# up down 게임
# computer(게임주최자) user(게임참가자)
# 객체 computer / user
# computer한태 필요한거 
# 1. 랜덤한 숫자 (게임하는 동안만 의미 있는거 ->지역변수로)
# 2. user 
# 3. user 가 말한 숫자(게임하는 동안만 의미 있는거 ->지역변수로)
# computer 가 할 액션 
# 1. 랜덤으로 숫자 뽑기
# 2. user한태 숫자 입력받기
# 3. 받은 숫자 판정하기
# 4. user 가 말한 숫자보다 크면 up이라고 말하기
# 5. user 가 말한 숫자보다 작으면 down 이라고 말하기
# 6. 맞추면 n턴만에 정답 이라고 말하기
# 7. turn수 세기
#  
# user 한태 필요한거
# 1. 맞출 숫자
# user 가 할 액션
# 1. 숫자 말하기

# computer는 user가 맞출때까지 액션 반복
# user도 맞출때까지 액션 반복
# from random import randint

# abcd 순서로 정리해두는데 Main역할 하는 건 맨밑으로
from random import randint


class Friend:
    def ask(self, user):
        userAnsTemp = user.tell()
        if 0 < userAnsTemp < 10001:
            return userAnsTemp
        return self.ask(user)
    
    def judge(self, gameAns, userAns):
        if gameAns == userAns:
            print("정답")
            return False
        elif gameAns > userAns:
            print("up")
        else:
            print("down")
        return True
    
    def tellResult(self, turn):
        print("%d턴만에 정답" % turn)

    def thinkAns(self):
        return randint(1, 10000)
    
    def start(self, user):
        turn = 0 #게임 하는 동안만 의미있는 turn수 -> 지역변수처리함
        gameAns = self.thinkAns() #게임하는 동안만 필요 ->지역변수처리로 
        print(gameAns)
        while True:
            turn += 1
            userAns = self.ask(user)
            if not self.judge(gameAns, userAns):
                break
        self.tellResult(turn)
    


class User:
    def tell(self):
        return int(input("뭐? : ")) #게임하는 동안만 필요하니까 지역변수로 함

##################################################
friend = Friend()
user = User()
friend.start(user)




################내가 끄적 댔건것####################
# class Computer:
#     def start(self, user):
#         user = self.ansUser() #게임 하는 동안만 의미 있는 숫자 -> 지역변수러 처리
#         self.ask(user)
#         self.gudge(user)
#         self.ansResult(user)
#     def computerNumber():
#         return randint(1, 10001)

#     def gudge(self, user, randint):
#         if user.ans == randint:
#             print("정답입니다.")
#             return False
#         elif randint > user.ans:
#             print("up")
#         else:
#             print("down")
#         return True


# class User:
#     pass
#     def ans(self):
#         self.num = int(input("숫자를 입력하세요 : ")) # 게임하는 동안만 필요 -> 지역변수로 처리