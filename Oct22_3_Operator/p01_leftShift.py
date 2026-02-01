# 와이파이  1 -> 1 << 0 = 1
# 24시간    2 -> 1 << 1 = 2
# 흡연실    3 -> 1 << 2 = 4
# 주차장    4 -> 1 << 3 = 8

# 1 -> 와이파이 나오게
# 2 -> 24시간 나오게
# 13 -> 와이파이, 흡연실, 주차장 나오게

wifi = 1
runTime = 2
smokeArea = 4
parkingLot = 8

#=============================내가 만든 소스
value = int(input("매장 특성 :"))
if value == 1:
    print("와이파이")
elif value == 2:
    print("24시간")
elif value == 3:
    print("흡연실")
elif value == 4:
    print("와이파이, 24시간")
elif value == 5:
    print("와이파이, 흡연실")
elif value == 7:
    print("와이파이, 24시간,흡연실")
elif value == 8:
    print("주차장")
elif value == 9:
    print("와이파이, 주차장")
elif value == 11:
    print("와이파이, 24시간, 주차장")
elif value == 13:
    print("와이파이, 흡연실, 주차장") 
elif value == 15:
    print("와이파이, 24시간, 흡연실, 주차장")
else:
    print("없음")


#===========썜이 만든거====================
value = int(input("매장 특성 :"))

if value >= 8:
    print("주차장")
    value -= 8
if value >= 4:
    print("흡연실")
    value -= 4
if value >= 2:
    print("24시간")
    value -= 2
if value >= 1:  #elif 안쓰는 이유는 조건에 각각 적용해야함
    print("와이파이")
    value -= 1
