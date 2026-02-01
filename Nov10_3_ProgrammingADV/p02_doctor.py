# 여기서는 받은 값 계산하는 부분탈모
from oracledb import connect

from jeong.jeongDBManager import JeongDBManager



class Doctor:
    def calculate(guest):
        con, cur = JeongDBManager.makeConcur("js/1234@195.168.9.58:1521/xe")
        # con = connect("js/1234@195.168.9.58:1521/xe") 
        guest.height /= 100
        guest.bmi = guest.weight / (guest.height * guest.height)
        if guest.bmi >= 39:
            guest.result = "고도비만"
        elif guest.bmi >= 32:
            guest.result = "중도비만"
        elif guest.bmi >= 30:
            guest.result = "경도비만"
        elif guest.bmi >= 24:
            guest.result = "과체중"
        elif guest.bmi >= 10:
            guest.result = "정상체중"

        sql = "insert into nov10_bmi " 
        sql += "values('%s','%.2f', " % (guest.name, guest.height)
        sql += "%.1f, %.2f, '%s')" %(guest.weight, guest.bmi, guest.result)
        print(sql)

        # cur = con.cursor()
        cur.execute(sql)
        con.commit()
        JeongDBManager.closeConCur(con, cur)
        # cur.close()
        # con.close()