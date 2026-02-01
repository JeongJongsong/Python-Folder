#  데이터 10TB -> 서버급 컴 여러대 병렬 전처리 -> Python 분석
#                 Hadoop : 병렬처리하는 기술(Linux에서만 실행가능한 Java)
#                 Elasticsearch :
# Python
#   분석/AI관련 문법 쉽게 잘 만들어져있음
#   컴 자원을 낭비하는 경향이 있음

# encoding/decoding
#   전세계적으로 utf08 방식 사용 엥간하면 이거???
#       Linux가 utf-8을 주력으로 써서
#       Windows가 euc-kr를 주력으로 쓰다가 -> utf-8쓰는 쪽으로
#   국내에서는 euc-kr이 그다음으로 많이 사용됨

f = open("C:\\Users/soldesk/Desktop/1030/p05.txt", "r", encoding="utf-8") #"r"은 읽기

# 1) 전체를 다 읽어서 str로
# data = f.read()
# print(data, type(data))

# 2) 다음 줄 읽어서 str로
# data = f.readline()
# print(data, type(data))
# data = f.readline()
# print(data, type(data))
# data = f.readline()
# print(data, type(data))
# data = f.readline()
# print(data, type(data))

# 3) 전체를 다 읽어서, \n 기준으로 나눠서 list로 (쓰기는 제일 편함)
# \n를 남겨놨음;;
data = f.readlines()
print(data, type(data))



f.close() 