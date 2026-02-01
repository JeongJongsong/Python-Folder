# 조건문 (Conditional Statement)

# 프로그램은 위 -> 아래, 왼쪽 -> 오른쪽
#   제어문(프로그램 실행 순서를 바꿔주는 문)
#       조건문
#       반복문

# 조건문 (Conditional Statement) : 조건 설정해서 실행할지말지
#   다른 PL들 : 조건문쓸때 if, switch
#   Python : if만 있음

# if 조건식A:    / 조건식 쓸때 가독성 차원에서 ()사용가능 쓰는게 가독성 좋음
#   A를 만족시킨 경우에 여기 실행 아님 실행안함
# elif 조건식B:
#   조건식A는x 틀림, B는O 경우 여기에서 실행 아니면 실행 안함
# elif 조건식C :
#   A/B는x, C는 o 경우 여기에서 실행 아니면 실행 안함
# .....쭉 elif쓰다가
# else:
#   위에 조건 만족되는거 하나도 없으면 여기서 실행

from re import A


mid = int(input("중간고사 : "))
final = int(input("기말고사 : "))
print("-------------------------------------")
avg = (mid + final) / 2
print("평균점수 : %.2f점" %avg)

# interpreter방식 언어 : 위에서부터 한줄씩 실행(Python)
#                       30번 줄 실행될때 a라는 변수가 있기만 하면 됨

# 평균점수가 90점 이상이면 잘했다.
# if avg >= 90:
#     print("매우 나이스다")
#     a = 10

# print(a)

# 평균점수 80이상 잘했다 출력
# 80 안되면 나가 출력
# 근데 70은 넘겼으면 열심히해라 출력
if avg >= 80:
    print("잘했다 풍성아")
else: #검사 횟수 줄어들고 소스도 짧아짐 
    print("나가 빡빡아")
    if avg >= 70:
        print("노력해라 빡빡아")

# 점수가 90점 이상이면 A
# 점수가 80 <= 점수 < 90 이면 B
# 70 <= 점수 <80
if avg >= 90:
    print("A") 
elif avg >= 80:   #elif = else+if 
    print("B")
elif avg >= 70:
    print("C")
elif avg >= 60:
    print("D")
else:
    print("F")

# 연습문제
#  이름, 키, 몸무게 받고 BMI 지수 계산

name = str("성명 : ")
height = float("키(m단위) : ")
weight = float("몸무게 :")
bmi = height / (weight)**2
# if bmi >= 39:
#     print("%s 님은 bmi %f(으)로 고도 비만입니다." % name, % bmi)
# else bmi >= 32:
