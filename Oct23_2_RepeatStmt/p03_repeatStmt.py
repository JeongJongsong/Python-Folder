# 1, 2, 3 순서로 출력
# 2
# 3
from re import L
from time import sleep


num = range(11)
for i in range(1, 4):
    print(i)
print("-------------------------") 
# 1 부터 10까지 출력
for i in range(1, 11):
    print(i)
print("-------------------------") 
#1부터 10까지 홀수만 
for i in range(1, 11, 2):
    print(i)
print("-------------------------") 
# 1부터 10까지 홀수만인데 역순으로
for i in range(11, 0, -2):
    print(i)
print("-------------------------") 
# 1~10까지 다 더한값
# 변수의 기본값 : 변수를 만들기만하고 값 안넣으면 어캐됨?  
#   -> Python은 값안넣는거 자체를 못함 a = 10 이런식으로 작성해서
#   -> 언어마다 다름 0/이상한값/없음
a = 0
for i in range(1,11):
    a += i
print(a)

# 1+3+5+7+9+11....+19 =?5
b = 0
for i in range(1, 20, 2):
    b += i
print(b)
print("-------------------------") 

# 2 x 1 = 2 
# 2 x 2 = 4
# .....
# 2 x 9 = 18
for i in range(1, 10):
    print("2 x %d = %d" % (i, 2 * i))
print("--------------------------------------------")

# 2 x 1 = 2 부터
# 9 x 9 = 81 까지
for dan in range(2, 10):
    for i in range(1, 10):
        print("%d x %d = %d" % (dan, i, dan * i))
print("--------------------------------------------")
# 2 x 1 = 2     3 x 1 = 3.....      9 x 1 = 9 이런 식으로 나오게
for i in range(1, 10):
    for dan in range(2, 10):
        print("%d x %d = %d" % (dan, i, dan * i), end="\t")
print()
print("--------------------------------------------")

# ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
# ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
# ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
# ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
for i in range(5):
    for j in range(5):
        print("ㅋ", end="")
        # sleep(0.5)
    print()
print("--------------------------------------------")
# ㅋ라미드 만들기
for i in range(10):
    for j in range(i + 1):
        print("ㅋ", end="")
        # sleep(0.5)
    print()

print("--------------------------------------------")
#역 ㅋ라미드 만들기
for i in range(10):
    for j in range(10 - i):
        print("ㅋ", end="")
        # sleep(0.5)
    print()
print("--------------------------------------------")
#ㅋ계단 만들기
for i in range(10):
    for j in range(i + 1):
        if i ==j :
            print("ㅋ", end="")
        else:
            print("  ", end="")
    print()
print("--------------------------------------------")
print("--------------------------------------------")
for i in range(10):
    for j in range(i):
        print("  ", end="")
    print("ㅋ")
print("--------------------------------------------")
# ㅋ
# ㅎㅎㅎ
# ㅋㅋㅋㅋㅋ
# ㅎㅎㅎㅎㅎㅎㅎ
# ㅋㅋㅋㅋㅋㅋㅋㅋㅋ
for i in range(5):
    for j in range(2 * i + 1):
        if i % 2 == 1:
            print("ㅎ", end="")
        
        print(end="")            
    print()
# 위 부분 놓쳤음 내일(금24)에 와서 영상보고 다시 해라



