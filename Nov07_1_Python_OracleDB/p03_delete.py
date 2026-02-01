# 이름 : 
# 삭제 성공

from os import name
from oracledb import connect

# 연결하기
con = connect("js/1234@195.168.9.58:1521/xe") # sqlplus써서 연결할때 주소쓰는 형식

# 삭제할 데이터확보
name = input("회사이름 : ")  # ->이게 콘솔부분

#->이게 DAO부분
sql = "delete from nov07_company " # 띄어쓰기 해놔야지 14번줄 where이랑 안붙음
sql += "where c_name = '%s'" % name 

cur = con.cursor()
cur.execute(sql)

if cur.rowcount == 1:
    print("삭제 성공")
else:
    print("삭제 실패")

cur.close()
con.close()

