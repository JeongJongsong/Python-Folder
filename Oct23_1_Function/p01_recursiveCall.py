# 숫자 하나 넣으면 팩토리얼 구하는 함수
# 1! = 1 = 1
# 2! = 1 X 2 = 2
# 3! = 1 x 2 x 3 = 6

# getFactorial(1) = 1
# getFactorial(2) = getFactorial(1) X 2 = 1 x 2  
# getFactorial(3) = getFactorial(2) x 3 = getFactorial(1) x 2 x 3 = 1 x 2 x 3 
def getFactorial(n):
    if n == 1:
        return 1 # 1이 아니면 밑에 함수로(return) 넘어가서 굳이 else 안써도됨
    return getFactorial(n - 1) * n

#########################################
a = getFactorial(3)
print(a)

print("--------------------------------")

# 숫자를 하나 넣으면 그 위치의 피보나치수열 값 구하는 함수
# 피보나치 앞의 두 수를 더한 값
# 1 2 3 4 5 6 7 - 위치
# 1 1 2 3 5 8 13
def getFibo(n):
    if (n == 1) or (n == 2):
        return 1
    return getFibo(n - 2) + getFibo(n - 1) 
# 왜 (n - 2) + (n - 1)이냐면
# 1과 2는 1이여서 그냥 1로 고정 시키고
# getFibo(3) = getFibo(1)값 + getFibo(2)값 이여서
# getFibo(4) = getFibo(2)값 + getFibo(3)값 이여서
# 피보나치수열 4의 값은 = 피보나치수열2의 값 + 피보나치수열3의 값 
#                 ---> 4앞의 두개 값(2의 값, 3의값)의 합이니까 
#                      4의값 = (4-2)+(4-1) -> 4의 값 = 2의 값 + 3의 값  


b = getFibo(5)
print(b)