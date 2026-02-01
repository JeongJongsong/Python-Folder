# 이름 :
# 수정할 가격 :
# 수정 성공

from oracledb import connect

# 연결
con = connect("js/1234@195.168.9.58:1521/xe")

# 수정할 데이터확보하는 부분
name = input("과자이름 : ")
name = "%" + name + "%"  
# -> SQL에서 포함된이름 걸러낼때 %이름% 이렇게 쓰는데
# Python에서 %이름% 이렇게 하려면 12번처럼 해야함
price = int(input("수정할 가격 : "))

sql = "update nov07_snack " # 띄어쓰기 해놔야지 14번줄 where이랑 안붙음
sql = "set s_price = %d " % price
sql += "where s_name like '%s'" % name

cur = con.cursor()
cur.execute(sql)

if cur.rowcount >= 1:
    print("수정 성공")
else:
    print("수정 실패")

cur.close()
con.close()