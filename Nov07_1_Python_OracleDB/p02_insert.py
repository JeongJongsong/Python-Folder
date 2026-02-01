from oracledb import connect

# 회사등록

# 연결
con = connect("js/1234@195.168.9.58:1521/xe") # sqlplus써서 연결할때 주소 쓰는 형식

# 데이터확보
name = input("회사이름 : ")
boss = input("사장이름 : ")
head = input("주소 : ")
employee = int(input("직원수 : "))

# SQL을 str로(; 이거 빼고)
sql = "insert into nov07_company values('%s', '%s', '%s', '%d')" %(name, head, boss, employee)

# DB관련 작업들 다 총괄해주는 매니저 객체 겸 결과
cur = con.cursor()

# str로 써놓은 SQL을 DB서버로 전송 + 원격실행 + 결과받아오기
cur.execute(sql)

# commit : 실제로 DB서버에 반영
# rollback : 반영시키지말고 취소하는거
# -> DBeaver가 자동 commit

# 실행결과
#   CUD(c/insert,update, delete) : 영향받은 데이터 수
#   R(read/selet) : 데이터
if cur.rowcount == 1:
    print("등록 성공")
    con.commit()
else:
    print("등록실패")

cur.close()  #매니져를 집에 보내는 그런 너낌 
# 연결해제
con.close()