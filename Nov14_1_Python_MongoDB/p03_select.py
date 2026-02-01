from pymongo import ASCENDING, DESCENDING, MongoClient

# 연결
con = MongoClient("195.168.9.58") #("")에 서버주소
db = con.nov14 # con.db명

# db.js배열명.find(객체명).sotr({필드명:1, 필드명:-1, ....}); {}객체로했는데
# ASCENDING 오름차순 --------- DESCENDING 내림차순
result = db.nov14_student.find().sort([("s_name", ASCENDING), ("s_name", DESCENDING)]);

# list취급해서 하나하나 돌려보면되고 / dict 모양이니까 저렇게 
for s in result:
    print(s["s_name"])
    print(s["s_age"])
    print("--------")

# 연결종료
con.close()