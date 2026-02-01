from pymongo import MongoClient

# OracleDB
#       table 속에 data
#       SQL라는 별개의 언어로 제어

# MongoDB
#       JavaScript배열 속에 JS객체 : Python의 list 안에 있는 dict랑 형태가 같음
#       JavaScript언어로 제어 : Python과 문법이 비슷
#       -> pymongo :MoongDB문법(명령어) 거의 그대로 쓰게 해줌

# 연결
con = MongoClient("195.168.9.58") #("")에 서버주소
db = con.nov14 # con.db명

# 데이터확보
name = input("이름 : ")
age = int(input("나이 : "))

# 명령어 + 서버로전송 + 원격 실행  한방에 가능함
result = db.nov14_student.insert_one({"s_name" : name, "s_age" : age});

# db.nov14_studet.delete_many -> 삭제
# db.nov14_studetn.update_many -> 수정

if result.acknowledged:
    print("등록 성공")
else:
    print("등록 실패") 

# 연결종료
con.close()