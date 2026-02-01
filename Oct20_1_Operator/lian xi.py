# buyPrice = int(input("구매한 물건 가격: "))
# payAmount = int(input("낸 돈 : "))
# changeAmount = int(payAmount - buyPrice)
# print("----------------------------------------------------------")
# print(
#     "물건 가격 : %s원, 낸 돈 : %s원, 거스름돈 %s원"
#     % (buyPrice, payAmount, changeAmount)
# )
# 돈5만원개수 = changeAmount // 50000
# 돈1만원개수 = changeAmount // 10000
# 돈5천원개수 = changeAmount // 5000
# 돈1천원개수 = changeAmount // 1000
# 돈5백원개수 = changeAmount // 500
# 돈1백원개수 = changeAmount // 100
# 돈5십원개수 = changeAmount // 50
# 돈1십원개수 = changeAmount // 10
# print("5만원 : %d, 1만원 : %d, 5천원 %d, 1천원 %d, 5백원 %d, 1백원 %d, 5십원 %d, 1십원 %d" \
#       % 돈5만원개수, 돈1만원개수, 돈5천원개수, 돈1천원개수, 돈5백원개수, 돈1백원개수, 돈5십원개수, 돈1십원개수)
# changeAmount %= 50000
# changeAmount %= 10000
# changeAmount %= 5000
# changeAmount %= 1000
# changeAmount %= 500
# changeAmount %= 100
# changeAmount %= 50
# changeAmount %= 10


lunch = int(input("점심값 : "))
day = int(input("일 수 : "))
metro = int(input("지하철 요금 : "))
time = int(input("하루 탑승 횟수 : "))
totalLunch = (lunch * day)
totalMetro = (metro * time * day)
totalMoney = (totalLunch + totalMetro)
print("총 점심값 : %s원" %totalLunch)
print("총 교통비 : %s원" %totalMetro)
print("한 달 총 비용 : %s원" %totalMoney)