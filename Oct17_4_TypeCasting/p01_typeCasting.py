# 폰 모델명 입력 받기
phoneModel = input("모델명 : ")
print("폰 모델명은 %s 입니다." % phoneModel)
# phoneModel 주소값
# phoneModel 자료형
print(id(phoneModel), type(phoneModel))
# 가격 입력, 주소값, 자료형
price = input("가격 : ")
price = int(price)
print("가격은 %d만원 입니다." % price)
print(id(price), type(price))
# 사용자는 숫자 or 문자로 입력 할 수 있음
#   => 그러면 숫자만 입력하게 하고 싶으면 어캐하냐
#   => 형변환(type casting) : 자료형을 바꿔주는 것 -> 자료형(변수명)
# int로 바꿈 -9번줄-

# --------------------------------------------------------------------
# 폰화면 크기 입력받기, 무조건 소수점이하 2자리로 나오게
# 변수 안쓸수 있으면 안쓰는게 best -> 메모리 사용량 감소
# 소스 짧으면 best -> 프로그램 용량 감소
# -> 소스 가독성에 영향 주지 않는 선에서 줄여서 쓰자
size = input("화면 크기 : ")
size = float(size)
print("화면크기 : %.2f in입니다." % size) 
#이소스 줄이면 밑에 처럼 2줄로 줄여짐
size = float(input("화면 크기 :"))
print("화면크기 : %.2f in입니다." % size) 
