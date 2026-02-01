from oracledb import connect
# sqlplus 아이디/비번@서버주소:포트/SID
con = connect("js/1234@195.168.9.58:1521/xe") # sqlplus써서 연결할때 주소 쓰는 형식

# 데이터 확보

sql = "SELECT * FROM nov07_company" # SQL(; 빼고)

cur = con.cursor() # DB관련 작업 총괄 객체 겸 결과

cur.execute(sql) # 실행

# for c in cur:
#     print(c[0])
#     print(c[1])

for name, head, boss, employee in cur:
    print(name)
    print(head)
    print("-------------") 

cur.close()
con.close()

