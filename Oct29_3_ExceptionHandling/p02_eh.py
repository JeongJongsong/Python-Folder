# x : 10 , y : 3
# 13 7 30 3.3  값 받아서 사칙연산 결과값 출력
#  파이썬에서 예외처리
#   try:
#       내용넣고
#   except 예외이름:
#       예외대응
#   -> 내용부분 실행핟가 문제없으면 없는거고
#   -> 내용부분 하다가 예외가 발생하면 -> 대응쪽으로 바로 이동해버리는 구조
x = int(input("x : "))
y = int(input("y : "))
z = [321, 501, 12]
print("------------------")

# y = 0 이면 20번줄 21번줄(하다가 ZDE터짐) 24번줄 - 25번줄

# try: # 수학적으로 나누기 0은 없음 
#     d = x / y #y에 0 넣으면 예외 발생하면 바로 18번 줄로 가버림
#     print(d)
#     print(z[y])
# except ZeroDivisionError:
#     print("나누기 0은 없다 멍청한놈아")
# except IndexError:
#     print("list에 그거 없어 이자시가")

# try:
#     d = x / y
#     print(d)
#     print(z[y])
# except:
#     print("뭔진 모르지만 어쨌든 문제 발생") #어디서 문제난건지 알빠 아니니까 퉁쳐라

try:
    d = x / y
    print(d)
    print(z[y])
except Exception as e:
    print(e)
    print("뭔진 모르지만 어쨌든 문제 발생") #어떤 문제가 발생한건지 알려줌 어딘지는 모름 