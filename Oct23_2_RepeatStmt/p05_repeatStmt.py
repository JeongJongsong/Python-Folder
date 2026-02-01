# 반복문 제어
#   break : 반복문 종료
#   continue : 턴 종료 
# for i in range(1, 101, 3):
#     if i % 10 == 0:
#         break
#     print(i)
# print("------------------------")
# # 1 ,4 ,7 ~~~ 
# for i in range(1, 101, 3):
#     if i % 10 == 0:
#         continue
#     print(i)
# print("------------------------")

# == True는 생략가능
# == False는 not 뭐뭐로 써

iBreak = False
for i in range(3): # 0부터 2까지 반복
    if iBreak == True: #그래서 여기 = Ture 생략가능
        break
    for j in range(3):
        if iBreak == True: #그래서 여기 = Ture 생략가능
            break
        for k in range(3):
            if k == 1:
                iBreak = True #그래서 여기 = Ture 생략가능
                break # for k in range(3):을 깨버림
            #내가 원하는 부분을 break 어캐 시켜야하나?
            # break로 for문 아에 깨버리는건 어캐?  for문 하나한에 조건식(if)달아야함
            print(i, j, k)

# while문 구조상
#   실제 작업내용은 밑에
#   조건은 위에 있음
#   -> 구조상 조건식 쓰기 애매함
# while True : #무한반복 만들어주고
#     a = input("뭐 : ") 
#     print(a)
#     if a == "나가": #조건식을 밑에 쓰고 조건에 맞으면
        # break       #break로 반복문 종료
        
#-----------------------------------
# 멘트 입력 받고 계속 출력
# 나가 입력하면 종료
# a = input("뭐 : ")
# print(a)
# while a != "나가":
#     a = input("뭐 : ")
#     print(a)

print("------------------------")
print("------------------------")
