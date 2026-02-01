# 과자 이름 :
# 가격 : 
# 중량 :
# -------------->파일에 저장해보기
# ........
# 과자 이름 :
# 가격 : 
# 중량 :
# -------------->파일에 저장해보기

# 이름 : 그만  쓰면 멈추도록 

# CSV(Comma Seprated Value)
#   값이 ,로 구분
#   엑셀에서 열리는데 MS Office가 utf-8을 소화못함(eur-kr은 정상 )

f = open("C:\\Users/soldesk/Desktop/Snack/snack.csv", "a", encoding= "utf-8")    
while True:
    name = input("이름 : ")
    if name == "그만":
        break
    price = int(input("가격 : "))
    weight = float(input("중량 : "))
    print("--------------------------")
    f.write("%s,%d,%.1f\n" %(name, price, weight))
f.close()