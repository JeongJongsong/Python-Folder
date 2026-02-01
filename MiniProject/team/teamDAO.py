
from team.team import Team
from jeong.jeongDBManager import JeongDBManager

class TeamDAO:
    def __init__(self):
        self.setAllTeamCount()
        self.teamPerPage = 3


#======================= 8) 팀 등록 부분 =======================
    def reg(self, team):
        try:
            con, cur = JeongDBManager.makeConcur("js/1234@195.168.9.58:1521/xe")
           
            sql = "insert into team "
            sql += "values(team_seq.nextval, '%s', '%s', '%s', '%s')" % (team.name, team.addr, team.coach, team.stadium)
        
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                return "등록 성공"
            else:
                return "등록 실패"
        
        except Exception as e:   # 나중에 지워도 되는 부분
            print(e)
            return "등록 실패"
        finally:
            JeongDBManager.closeConCur(con, cur)

#======================= 9) 팀 정보 수정 부분 ========================================
    def update(self, name, choice, newInfo):
        try:
            con, cur = JeongDBManager.makeConcur("js/1234@195.168.9.58:1521/xe")

            if choice == "1":
                sql = "UPDATE team SET t_coach = '%s' WHERE t_name = '%s'" %(newInfo, name)
            elif choice == "2":
                sql = "UPDATE team SET t_stadium = '%s' WHERE t_name = '%s'" %(newInfo, name)
            else:
                return "잘못된 항목 선택입니다."

            cur.execute(sql)
            if cur.rowcount >= 1:
                con.commit()
                return "팀 정보 수정 성공"
            else:
                return "팀 정보 수정 실패"
        
        except Exception as e: #뭔 예외인지는 모르겠지만 걍 진행시켜줘 
            print(e)
            return "팀 정보 수정 실패"
        finally:
            JeongDBManager.closeConCur(con, cur)
#======================= 9) 팀 삭제 부분 ========================================
    def delete(self, team_name):
        try:
            con, cur = JeongDBManager.makeConcur("js/1234@195.168.9.58:1521/xe")

            sql = "delete from team "
            sql += "where t_name = '%s'" % team_name

            cur.execute(sql)
            
            if cur.rowcount== 1:
                con.commit()
                return "팀 삭제 성공"
            else:
                return "팀 삭제 실패!! 팀명을 제대로 입력하세요"
        
        except Exception as e: #뭔 예외인지는 모르겠지만 걍 진행시켜줘 
            print(e)
            return "팀 삭제 실패"
        finally:
            JeongDBManager.closeConCur(con, cur)


#======================= 11) 특정 팀 조회 부분 ========================================
    def getTeam(self, searchTxt):
            try:
                con, cur = JeongDBManager.makeConcur("js/1234@195.168.9.58:1521/xe")
                
                searchTxt = "%" + searchTxt + "%"
    
                sql = "SELECT * "
                sql += "FROM ( "
                sql += "    SELECT rownum AS rn, t_name, t_addr, t_coach, t_stadium "
                sql += "    FROM ( "
                sql += "    SELECT t_name, t_addr, t_coach, t_stadium "
                sql += "    FROM team "
                sql += "         WHERE (t_name LIKE '%s') " % (searchTxt)
                sql += "    ) "
                sql +=") "
                cur.execute(sql)
    
                teams = []
                for _, name, addr, coach, stadium in cur:
                    t = Team(_, name, addr, coach, stadium)
                    teams.append(t)
                return teams
            except Exception as e:   # 나중에 지워도 되는 부분
                print(e)
                return []
            finally:
                JeongDBManager.closeConCur(con, cur)

#--------------------- 12) 전체 팀 조회 부분 ---------------------
    def getAll(self):
        try:
            con, cur = JeongDBManager.makeConcur("js/1234@195.168.9.58:1521/xe")

            sql = "SELECT * FROM team ORDER BY t_name"
            cur.execute(sql)

            teams = []
            for no, name, addr, coach, stadium in cur:
                t = Team(no, name, addr, coach, stadium)
                teams.append(t)
            return teams
        
        except Exception as e: #예외 있어도 걍 진행시키는 문법
            print(e)
            return []
        finally:
            JeongDBManager.closeConCur(con,cur)

#--------------------- 팀 이름만 가져오기 ---------------------
    def getTeamName(self):
        try:
            con, cur = JeongDBManager.makeConcur("js/1234@195.168.9.58:1521/xe")

            sql = "SELECT  t_name FROM team"
            cur.execute(sql)

            teams = []
            for team in cur:
                t = Team(None, team[0], None, None, None)
                teams.append(t)
            return teams
        
        except Exception as e: #예외 있어도 걍 진행시키는 문법
            print(e)
            return []
        finally:
            JeongDBManager.closeConCur(con,cur)
#######################################################################

    def setAllTeamCount(self): #전체 팀 수 카운팅
        try:
            con, cur = JeongDBManager.makeConcur("js/1234@195.168.9.58:1521/xe")
            sql = "select count(*) from team"
            cur.execute(sql)

            for result in cur:
                self.allTeamCount = result[0]
         
        except Exception as e:   # 나중에 지워도 되는 부분
            print(e)
        finally:
            JeongDBManager.closeConCur(con, cur)

