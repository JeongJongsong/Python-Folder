# 유지보수의 시대 -> 소스 알아보기 편해야 함

###########################################
# 이름이 홍길동, 국어100, 영어90, 수학80 학생
# 정보출력


from os import name


class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def printInfo(self):
        print(self.name, self.kor, self.eng, self.math)
#############################################################
s1 = Student("홍길동", 100, 90, 80)
s2 = Student("김길동", 90, 23, 34)

score = [
    s1,
    s2,
    Student("홍박사", 0, 30, 80),
    Student("홍길순", 82, 21, 44),
]

score[0].printInfo() # 첫 번째 학생의 모든 정보 출력(메소드 활용 가능)
print(score[2].kor)# 세 번째 학생의 국어점수(소스 보기도 쉬움)
print("-------------------------")

# 학생객체를 넣으면, 학생의 이름이 리턴되는 함수
# def getName(s):
#     return s.name

# test = getName(score[2])
# print(test)

# test = (lambda s:s.name)(score[2])
# print(test)

# 정렬(이름 가나다순)
# socre라는 list에는 학생객체가 있음
# 정렬은 학생 이름으로 하고싶음
# 학생객체를 넣으면 그 학생이름 나오는거로
# score.sort(key = lambda s:s.name)

# 정렬(평균점수 낮은 순으로)
# def getAvg(s):
#     return (s.kor + s.eng + s.math) / 3
# test = getAvg(score[1])
# 위에껄 lambda로 바꾸면 밑
test = (lambda s:s.kor + s.eng + s.math / 3)(score[1])
print(test)

score.sort(key=lambda s:s.kor + s.eng + s.math, reverse=True)

print("---------------")
for s in score:
    s.printInfo()

