
from random import choice
from team.teamDAO import TeamDAO
from team.team import Team
from player.player import Player


 # 쌤이랑 같이한거에서 상품product이 선수 포지션
# 쌤이랑 같이한거에서 판매자seller가 팀 포지션
class ConsoleScreen:
    def showMainMenu():
        print("------------------")
        print("1) 선수 등록,"" ""2) 선수 수정,"" ""3) 선수 삭제")
        print("4) 선수 조회,"" ""5) 포지션 조회,"" ""6) 팀별 선수 조회")
        print("7) 전체 선수 조회,"" ""8) 팀 등록,"" ""9) 팀 수정")
        print("10) 팀 삭제,"" ""11) 팀 조회,"" ""12) 전체 팀 조회")
        print("------------------")
        return input("조회하고싶은 항목의 번호를 입력해주세요. : ")
    
    def showRegPlayerMenu(): # 1) 선수 등록 부분
        name = input("선수 이름 : ")
        birthday = input("선수 생년월일 : ")
        nationality = input("선수 국적 : ")
        position = input("선수 포지션 : ")
        backNo = input("선수 등번호 : ")
        t_name = input("소속팀번호 1)맨유 2)첼시 3)토트넘 : ")
        return Player(name, birthday, nationality, position, backNo, t_name)
    
    def showPlayerUpdate(): # 2)선수 수정 부분
        name = input("수정할 선수 이름 : ")
        print("------------")
        print("1) 포지션")
        print("2) 등번호")
        print("3) 팀")
        choice = input("수정할 항목 번호 : ")
        newInfo = input("수정 내용 : ")
        return name, choice, newInfo

    def showPlayerDelete(): # 3) 선수 삭제 부분
        name = input("선수 이름 : ")     
        return name


    def showPlayer2(players): #  4)특정 선수 조회
        for player in players:
            print("------------")
            print(player.name)
            print(player.birthday)
            print(player.nationality)
            print(player.position)
            print(player.backNo)
            print(player.t_name)
            print("------------")

    def showPlayerPosition(players): #  5)포지션별 선수 조회
        for player in players:
            print(player.name)
            print(player.nationality)
            print(player.position)
            print(player.backNo)
            print(player.t_name)
            print("------------")

    def showPlayerTeam(players): #  6) 팀별 선수 조회
        for player in players:
            print("------------")
            print(player.name)
            print(player.nationality)
            print(player.position)
            print(player.backNo)
            print(player.t_name)
            print("------------")

    def showPlayers(players): # 7) 전체 선수 조회
        for player in players:
            print("------------")
            print(player.name)
            print(player.birthday)
            print(player.nationality)
            print(player.position)
            print(player.backNo)
            print(player.t_name)
            print("------------")

    def showRegTeamMenu(): # 8) 팀 등록 부분
        name = input("팀 이름 : ")
        addr = input("연고지 이름 : ")
        coach = input("감독 이름 : ")
        stadium = input("홈구장 이름 : ")
        return Team(None, name, addr, coach, stadium)    

    def showTeamUpdate(): # 9) 팀 수정 부분
        teamDAO = TeamDAO()
        teamAllName = teamDAO.getTeamName()
        for t in teamAllName:
            print(t.name, end="/ ")
        name = input("\n""수정할팀 이름 : ")
        print("------------")
        print("1) 감독," " " "2) 경기장")
        choice = input("수정할 항목 번호 : ")
        newInfo = input("수정 내용 : ")
        return name, choice, newInfo  
        

    def showTeamDelete(): # 10) 팀 삭제 부분
        teamDAO = TeamDAO()
        teamAllName = teamDAO.getTeamName()
        for t in teamAllName:
            print(t.name, end="/ ")
        return input("\n""팀 이름 : ") 

    def showTeams(teams): # 11) 특정 팀 조회
        
        for team in teams:
            print("------------")
            print(team.name)
            print(team.addr)
            print(team.coach)
            print(team.stadium)
            print("------------")
            
    def showTeams(teams): # 12) 전체 팀 조회
        for team in teams:
            print("------------")
            print(team.name)
            print(team.addr)
            print(team.coach)
            print(team.stadium)
            print("------------")

    def showResult(result):
        print(result)

    def showSearchName():
        return input("선수이름 : ") 
    
    def showSearchPosition():
        return input("포지션 : ") 
    
    def showSearchTeam():
        teamDAO = TeamDAO()
        teamAllName = teamDAO.getTeamName()
        for t in teamAllName:
            print(t.name, end="/ ")
        return input("\n""팀 이름 : ") 
    
    def showSearch():
        return input("선수이름 : ") 
    
    def showSearchMenu():
        return input("선수이름 : ") 
    