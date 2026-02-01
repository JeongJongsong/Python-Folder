# range 범위표현, 규칙적인 list 필요할때
a = range(10)  # 0 ~ (10-1)
a = range(2, 10)  # 2 ~ (10-1)
a = range(2, 10, 3)  # 2 ~ (10-1), 3칸씩
print(a)
print(type(a))

# list 1 ~ 20 까지
b = range(1, 21)
b = list(b)  # range를 list로
print(b)
print(type(b))

#===============================================================================
# tuple --> () 사용 / 특징은 list랑 같음
# 데이터들 표현X
# tuple이 "Python의 특수한 문법의 기반이 된다"
c = (10, 54, 21, 11, 3, 21, 10)
print(c)
print(type(c))
print(c[2])

# x와 y값을 서로 어캐 바꿈?
x = 10
y = 20
# (x, y) = (y, x)  # --> x = 20 / y = 10
x, y = y, x #() 생략가능 
print(x)
print(y)
print("==============================")
# q = 100
# w = 200
# e = 300
#  한줄로 만드면 
# (q, w, e) = (100, 200, 300)
q, w, e = 100, 200, 300         #() 생략가능
(q, w, e) = (w, e, q)
print(q)
print(w)
print(e)
