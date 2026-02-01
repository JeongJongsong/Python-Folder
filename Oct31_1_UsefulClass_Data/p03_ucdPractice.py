# 1) snack.csv 읽어서 한줄씩 콘솔출력 
# 2) 이름따로 가격따로 다 따로따로 나오게 
# 3) 과자(이름, 가격, 중량, 정보출력기능)
# 4) 객체 list
# 제일비싼과자정보, 각 과자g당 가격, .....



class Snack:
    def __init__(self, line):
        line = line.replace("\n", "")
        line = line.split(",")
        self.name = line[0]
        self.price = int(line[1])
        self.weight = float(line[2])

    def printInfo(self):
        print(self.name, self.price, self.weight)

##################################################### 
f = open("C:/Users/soldesk/Desktop/Snack/snack.csv", "r", encoding="utf-8")
snacks = []
for line in f.readlines():
    s = Snack(line)
    snacks.append(s)
f.close()

# 전체과자 정보출력
for s in snacks:
    s.printInfo()
print("-----------------")
# 제일 비싼과자 정보출력 정렬해보란 소리
snacks.sort(key=lambda s: s.price, reverse=True)
snacks[0].printInfo()
print("-----------------")
# g당 가격이 가장 싼 과자 정보출력
snacks.sort(key=lambda s: s.price / s.weight)
snacks[0].printInfo()