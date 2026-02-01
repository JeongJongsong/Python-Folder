# 로또 번호 자동으로 나오게
# 1~45 / 랜덤숫자 중복 없이 6개
#  


from random import randint

def pick(i, lotto):
    l = randint(1, 46)
    for j in range(i):
        if l == lotto[j]:
            return pick(i, lotto)
    return l
######################################
lotto = [] # 숫자 담을 빈 그릇 만듦
for i in range(6):   #작업 반복
    l = pick(i, lotto)
    lotto.append(l)

print(lotto)


# 내가 끄적였던 흔적
# from random import randint
# from tkinter import N


# numTable = (1,46)
# def num(numTable):
#     for i, v in enumerate(numTable):
#         if i != 0:
#             print("%d" % v)

# def choiceNum():
#     for i in range(6):
#         n = randint(1,46)
#         print(n)
#     if n[0] == n[1]:
#         return choiceNum()
    