# AOP적인 생각 : 어떤 DB작업을 하던지 공통된 부분이 존재함
#               -> 그래서 따로 정리할 필요 있음
# 그 정리하는거 이번 프로젝트 뿐만 아니라, 계속 사용되겠다 싶은걸 도구로 만들어놓으라고 띱띱띱!!
# => DB관련 라이브러리(도구)를 만들어야겠다 ~
# -> 특정상황 전용, 일반적, 다양한 상황에 대응할 수 있는 라이브러리 만들어봐

from oracledb import connect

# Nov10_3_ProgrammingADV.p02_docotor 내용 보고 하는중임
class JeongDBManager:
    @staticmethod
    def makeConcur(info): #->()안에는 연결정보받아서
        con = connect(info)
        cur =con.cursor()
        return con, cur
    
    @staticmethod
    def closeConCur(con, cur):
        cur.close()
        con.close()