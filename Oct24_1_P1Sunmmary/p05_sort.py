# list를 넣으면 정렬(오름차순)해주는 함수

# 오름차순 해주는 함수 불러

from math import trunc
import select


# def bubbleSort(l):
#     for turn in range(len(l) - 1): #0 ~3 턴
#         for i in range(len(l) - 1 - turn): # 0 ~ 3
#             if l[i] > l[i + 1]:
#                 l[i], l[i + 1] = l[i + 1], l[i]



# def selectionSort(l):
#     for i, v in range(len(l) - 1): # 0 ~ 3
#         if l[i] > l[i + 1]:
#             l[i] and l[i + 1] = l[i + 1]

# l의 list 중에서 최소값을 어캐 고르냐고?!!

def selectionSort(l):
    for turn in range(0, len(l)-1): # 0 ~ 3까지
        min = l[turn] # 일단은 turn번이 최소값이라고 치고
        minIndex = turn # 최소값이 turn번에 있다고 하고
        for i in range(turn + 1, len(l)): # 1~4까지
         if min > l[i]: # 최소값보다 i번째 있는게 작으면
             min = l[i] # 그게 최소값
             minIndex = i # 최소값은 i번째 있는거
        l[turn], l[minIndex] = l[minIndex], l[turn] # turn번이랑 최소값 있는 위치 자리 바꾸기

#########################################
l = [321, 21, 35, 485, 22, 685, 913, 210, 2, 13]

# bubbleSort(l)
selectionSort(l)
print(l)