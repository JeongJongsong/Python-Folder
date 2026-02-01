from random import randint


lotto = []  #lotto라는 빈그릇 만들어 
while True: #아래 소스들 반복해 
    l = randint(1, 45) # l은 1에서45중 랜덤한 숫자 하나 
    lotto.append(l) # 일단 넣고
    lotto = set(lotto) # set = 중복없애고, 순서는 랜덤으로
    lotto = list(lotto) # 다시 list로 list

    if len(lotto) == 6:
        break

print(lotto)




from random import randint

all_lotto = []   # 로또 5세트 저장

for i in range(10):
    lotto = []

    while True:
        lotto.append(randint(1, 45))
        lotto = list(set(lotto))

        if len(lotto) == 6:
            break

    all_lotto.append(lotto)

    print(sorted(lotto))