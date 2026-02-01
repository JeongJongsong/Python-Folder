# 연습문제
#  이름, 키, 몸무게 받고 BMI 지수 계산

from time import sleep


name = input("성명 : ")
height = float(input("키(m단위) : "))
weight = float(input("몸무게 :"))
print("-------------------------------")
bmi = weight / (height * height)
print("BMI : %.2f" %bmi)
# if bmi >= 39:
#     print("%s님의 bmi는 %.2f(으)로 고도 비만입니다." %(name, bmi))
# elif bmi >= 32:
#     print("%s님의 bmi는 %.2f(으)로 중도비만입니다." %(name, bmi))
# elif bmi >= 30:
#     print("%s님의 bmi는 %.2f(으)로 경도비만입니다." %(name, bmi))
# elif bmi >= 24:
#     print("%s님의 bmi는 %.2f(으)로 과체중입니다." %(name, bmi))
# elif bmi >= 10:
#     print("%s님의 bmi는 %.2f(으)로 정상체중입니다." %(name, bmi))
# else:
#     print("%s님의 bmi는 %.2f(으)로 저체중입니다." %(name, bmi))
################위 내용을 좀 더 짧고 간결? 하게 만들면 밑에################
result = "저체중"
if bmi >= 39:
    result = "고도비만"
elif bmi >= 32:
    result = "중도비만"
elif bmi >= 30:
    result = "경도비만"
elif bmi >= 24:
    result = "과체중"
elif bmi >= 10:
    result = "정상체중"
print("%s님의 bmi는 %.2f(으)로 %s입니다." %(name, bmi, result))

sleep(10)

# 일반인들이 실행하기 용이하게
# 실행파일까지 만들어줘야함
# 1) bat파일
# 2) pyinstaller

# .bat -> cmd 명령어 써놓는 파일
#   .bat 파일 싱행하면 그 명령어가 실행됨