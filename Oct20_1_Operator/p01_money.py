buyPrice = int(input("구매한 물건 가격: "))
payAmount = int(input("낸 돈 : "))
changeAmount = int(payAmount - buyPrice)
print("----------------------------------------------------------")
print(
    "물건 가격 : %s원, 낸 돈 : %s원, 거스름돈 %s원"
    % (buyPrice, payAmount, changeAmount)
)
# 거스름돈에 맞춰서 화폐단위 주기 ex) 340원 남았으면 100원짜리3개 10원짜리 4개 / 250원이면100짜리2,50짜리1/3560원,1000/3, 500/1, 50/1, 10/1

돈5만원개수 = changeAmount // 50000
print("5만원 : %d" % 돈5만원개수)
changeAmount %= 50000

돈1만원개수 = changeAmount // 10000
print("1만원 : %d" % 돈1만원개수)
changeAmount %= 10000

돈5천원개수 = changeAmount // 5000
print("5천원 %d" % 돈5천원개수)
changeAmount %= 5000

돈1천원개수 = changeAmount // 1000
print("1천원 %d" % 돈1천원개수)
changeAmount %= 1000

돈5백원개수 = changeAmount // 500
print("5백원 %d" % 돈5백원개수)
changeAmount %= 500

돈1백원개수 = changeAmount // 100
print("1백원 %d" % 돈1백원개수)
changeAmount %= 100

돈5십원개수 = changeAmount // 50
print("5십원 %d" % 돈5십원개수)
changeAmount %= 50

돈1십원개수 = changeAmount // 10
print("1십원 %d" % 돈1십원개수)
changeAmount %= 10

print("5만원 : %d, 1만원 : %d, 5천원 : %d, 1천원 : %d, 5백원 : %d, 1백원 : %d, 5십원 : %d, 1십원 : %d," \
      % (돈5만원개수, 돈1만원개수, 돈5천원개수, 돈1천원개수, 돈5백원개수, 돈1백원개수, 돈5십원개수, 돈1십원개수))

