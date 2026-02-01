# 실무가면 여기가 내가 만져야될 부분
from jeong.jeongDBManager import JeongDBManager

class CompanyDAO:
    def reg(company):
        con,cur = JeongDBManager.makeConcur("js/1234@195.168.9.58:1521/xe")
        sql = "insert into nov07_company "
        sql += "values('%s', '%s', '%s', %d)" % (company.name, company.head, company.boss, company.employee)
        cur.execute(sql)

        if cur.rowcount == 1:
            con.commit()
            JeongDBManager.closeConCur(con, cur)
            return "등록 성공"
        else:
            JeongDBManager.closeConCur(con, cur)
            return "등록 실패"