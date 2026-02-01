from math import ceil
from player.player import Player
from jeong.jeongDBManager import JeongDBManager


class PlayerDAO:
    def __init__(self):
        self.setAllPlayerCount()
        self.playerPerPage = 5

#======================= 1) 선수등록 부분 ========================================
    def reg(self, player):
        try:
            con, cur = JeongDBManager.makeConcur("js/1234@195.168.9.58:1521/xe")

            sql = "INSERT INTO player "
            sql += "values('%s', '%s', '%s', '%s', '%s', '%s')" % (player.name, player.birthday, player.nationality, player.position, player.backNo, player.t_name)

            cur.execute(sql)
            if cur.rowcount== 1:
                con.commit()
                return "선수등록 성공"
            else:
                return "선수등록 실패"
        
        except Exception as e: #뭔 예외인지는 모르겠지만 걍 진행시켜줘 
            print(e)
            return "선수등록 실패"
        finally:
            JeongDBManager.closeConCur(con, cur)

#======================= 2) 선수 수정 부분 ========================================
    def update(self, name, choice, newInfo):
        try:
            con, cur = JeongDBManager.makeConcur("js/1234@195.168.9.58:1521/xe")

            if choice == "1":
                sql = "UPDATE player SET p_position = '%s' WHERE p_name = '%s'" %(newInfo, name)
            elif choice == "2":
                sql = "UPDATE player SET p_backNo = '%s' WHERE p_name = '%s'" %(newInfo, name)
            elif choice == "3":    
                sql = "UPDATE player SET p_t_no = '%s' WHERE p_name = '%s'" %(newInfo, name)
            else:
                return "잘못된 항목 선택입니다."

            cur.execute(sql)
            if cur.rowcount >= 1:
                con.commit()
                return "선수 정보 수정 성공"
            else:
                return "선수 정보 수정 실패"
        
        except Exception as e: #뭔 예외인지는 모르겠지만 걍 진행시켜줘 
            print(e)
            return "선수수정 실패"
        finally:
            JeongDBManager.closeConCur(con, cur)

#======================= 3) 선수 삭제 부분 ========================================
    def delete(self, player_name):
        try:
            con, cur = JeongDBManager.makeConcur("js/1234@195.168.9.58:1521/xe")

            sql = "delete from player "
            sql += "where p_name = '%s'" % player_name

            cur.execute(sql)
            
            if cur.rowcount== 1:
                con.commit()
                return "선수삭제 성공"
            else:
                return "선수삭제 실패"
        
        except Exception as e: #뭔 예외인지는 모르겠지만 걍 진행시켜줘 
            print(e)
            return "선수삭제 실패"
        finally:
            JeongDBManager.closeConCur(con, cur)


#======================= 4) 특정 선수 조회 부분 ========================================
    def get(self, searchTxt):
        try:
            con, cur = JeongDBManager.makeConcur("js/1234@195.168.9.58:1521/xe")
            
            searchTxt = "%" + searchTxt + "%"

            sql = "SELECT * "
            sql += "FROM ( "
            sql += "    SELECT rownum AS rn, p_name, p_birthday, p_nationality, p_position, p_backNo, t_name "
            sql += "    FROM ( "
            sql += "    SELECT p_name, p_birthday, p_nationality, p_position, p_backNo, t_name "
            sql += "    FROM team, player "
            sql += "    WHERE t_no = p_t_no "
            sql += "         AND (p_name LIKE '%s' or p_nationality LIKE '%s' or p_position LIKE '%s') " % (searchTxt, searchTxt, searchTxt)
            sql += "       ORDER BY p_name "
            sql += "    ) "
            sql +=") "
            cur.execute(sql)
            
            if cur.rowcount == 1:
                print("검색 성공")
            else:
                print("그딴선수는 없습니다. 다시 검색하세요.")
            
            players = []
            for _, name, birthday, nationality, position, backNo, t_name in cur:
                p = Player(name, birthday, nationality, position, backNo, t_name)
                players.append(p)
            return players
        except Exception as e:   # 나중에 지워도 되는 부분
            print(e)
            return None
        finally:
            JeongDBManager.closeConCur(con, cur)

#======================= 5) 포지션 조회 부분 ========================================
    def get2(self, searchTxt):
        try:
            con, cur = JeongDBManager.makeConcur("js/1234@195.168.9.58:1521/xe")
            
            searchTxt = "%" + searchTxt + "%"

            sql = "SELECT * "
            sql += "FROM ( "
            sql += "    SELECT rownum AS rn, p_name, p_birthday, p_nationality, p_position, p_backNo, t_name "
            sql += "    FROM ( "
            sql += "    SELECT p_name, p_birthday, p_nationality, p_position, p_backNo, t_name "
            sql += "    FROM team, player "
            sql += "    WHERE t_no = p_t_no "
            sql += "         AND (p_position LIKE '%s') " % (searchTxt)
            sql += "       ORDER BY p_name "
            sql += "    ) "
            sql +=") "
            cur.execute(sql)

            players = []
            for _,no, name, nationality, position, backNo, t_name in cur:
                p = Player(no, name, nationality, position, backNo, t_name)
                players.append(p)
            return players
        except Exception as e:   # 나중에 지워도 되는 부분
            print(e)
            return None
        finally:
            JeongDBManager.closeConCur(con, cur)

#======================= 6) 팀별 선수 조회 부분 ========================================
    def get3(self, searchTxt):
        try:
            con, cur = JeongDBManager.makeConcur("js/1234@195.168.9.58:1521/xe")
            
            searchTxt = "%" + searchTxt + "%"

            sql = "SELECT * "
            sql += "FROM ( "
            sql += "    SELECT rownum AS rn, p_name, p_birthday, p_nationality, p_position, p_backNo, t_name "
            sql += "    FROM ( "
            sql += "    SELECT p_name, p_birthday, p_nationality, p_position, p_backNo, t_name "
            sql += "    FROM team, player "
            sql += "    WHERE t_no = p_t_no "
            sql += "         AND (t_name LIKE '%s') " % (searchTxt)
            sql += "       ORDER BY p_name "
            sql += "    ) "
            sql +=") "
            cur.execute(sql)

            players = []
            for _,no, name, nationality, position, backNo, t_name in cur:
                p = Player(no, name, nationality, position, backNo, t_name)
                players.append(p)
            return players
        except Exception as e:   # 나중에 지워도 되는 부분
            print(e)
            return None
        finally:
            JeongDBManager.closeConCur(con, cur)

#======================= 7) 전체선수 조회부분 ========================================
    def getAll(self):
        try:
            con, cur = JeongDBManager.makeConcur("js/1234@195.168.9.58:1521/xe")

            sql = "SELECT * FROM player ORDER BY p_name"
            cur.execute(sql)

            players = []
            for name, birthday, nationality, position, backNo, p_t_no in cur:
                p = Player(name, birthday, nationality, position, backNo, p_t_no)
                players.append(p)
            return players
        
        except Exception as e: #예외 있어도 걍 진행시키는 문법
            print(e)
            return None
        finally:
            JeongDBManager.closeConCur(con,cur)

#======================= 전체 선수 수 세는 메서드 =====================
    
    def setAllPlayerCount(self): #전체 선수 수 세는 메서드
        try:
            con, cur = JeongDBManager.makeConcur("js/1234@195.168.9.58:1521/xe")
            sql = "select count(*) from player"
            cur.execute(sql)

            for result in cur:
                self.allPlayerCount = result[0] # allPlayerCount라는 멤버변수에 숫자 세팅
         
        except Exception as e:   # 나중에 지워도 되는 부분
            print(e)
        finally:
            JeongDBManager.closeConCur(con, cur)