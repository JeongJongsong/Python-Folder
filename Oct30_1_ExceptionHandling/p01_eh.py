# Exception Handling 예외처리
#   try:
#       내용
#   except 이름:
#       대응
#   except 이름:
#       대응
#   .......
#   else
#   try부분 하는동안 아무문제 없으면 진행됨 ->파이썬에만 있음
#   finally:
#       try부분 하는 동안 문제가 있든 없든 무조건 실행되는데
#       return보다 먼저 실행됨 -> 중간에 return있을때 사용하는게 finally

# y에 1쓰면 : #1-#2-#3-#4-#5-#6 순서로 진행됨
# y에 ㅋ 쓰면: #1-#2-#3(VE발생)-#8-#9
# y에 0쓰면 : #1-#2-#3-#4(ZDE발생)-#6-#7


try: #1
    x = int(input("x : ")) #2
    y = int(input("y : ")) #3
    z = x / y #4
    print(z) #5
except ZeroDivisionError: #6
    print("나누기 0은 없다 이자시가") #7
except ValueError: #8
    print("숫자를 넣어라 멍청아") #9
else:
    print("정상계산 완료다 이자시가") #-> 가독성떄문에 쓰는 느낌
finally: #이부분을 진짜 하고싶으면 굳이 finally
    print("문제가 있긴한데 어쨌는 여기는 무조건 실행됨")