# 숫자를 1개 넣으면 1+2+3+4+5 ..... 그 숫자 = ?
# 1부터 입력한 숫자 까지 다 더해주는 함수 만들어봐라
# 팩토리얼을 만들어라

# 함수 recursive call (재귀적호출)
# 함수내에서 함수본인을 계속 호출해서 반복생기게 하는 테크닉


def getHap(x):
    if x == 1:
        return 1
    else:
        return getHap(x - 1) + x

############
x = getHap(10)
print(x)

