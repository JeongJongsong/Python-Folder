# collection : 데이터들을 표현할때 사용
# 1. list : 제일 많이 사용 -> NmuPy(list기능 개선판) ----->  [] 대괄호 사용 / 어떤 데이터가 있는지 보여줌
a = [1, 1, 2, 3, 4, 1, 2, 34, 47, 76, 89]
print(a)
print(a[3])
# 2. set  : 중복된 데이터 없애줌, 단 순서 랜덤으로 나옴 -> 주력으로 사용하기엔 부적합
# 1) 데이터 받아와서 list로
# 2) 근데 중복을 없애야 한다면??

a = set(a) # list를 set으로
a = list(a) #set를 list로
print(a)

# 3. dict : 순서개념X, 키:값 -> 활용도 높음 ----> {} 중괄호 씀
student = {"홍길동": {"국어": 50, "영어": 30}, 
           "길길동": 80}
print(student["길길동"])
# 다차원list? : 알아보기 힘듦
# dict + list 조합으로 표현
print(student["홍길동"]["국어"])
print(list(student.keys())) # ---> 키 값만 추출해줌

print("제갈길동" in student)# 학생중에 제갈길동이 있나 확인해보고 싶을때 / 있으면 true 없으면 false