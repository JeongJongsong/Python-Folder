# 계산기 만들어서
# 숫자(x,y,z,...):  10, 2, ㅋ, 5, asd, 3 
# 합계 :
# 평균 :

numbers = input("숫자(x, y, z, ...) : ")
print("-----------------------------------")
numbers = numbers.split(",")

hap = 0
cnt = len(numbers)
for n in numbers:
    try:
        hap += int(n)
    except:
        cnt -= 1

print("합계 : %d" % hap)
print("평균 %.1f" % (hap / cnt))
