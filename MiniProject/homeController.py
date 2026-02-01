
from team.teamDAO import TeamDAO
from consoleScreen import ConsoleScreen
from player.playerDAO import PlayerDAO


if __name__ == "__main__":
    playerDAO = PlayerDAO()
    teamDAO = TeamDAO()
    while True :
        menu = ConsoleScreen.showMainMenu()

        if menu =="13":
            break
        
        elif menu == "1":   #consoleScreen에서 선수등록 부분
            player = ConsoleScreen.showRegPlayerMenu()
            result = playerDAO.reg(player)
            ConsoleScreen.showResult(result)

        elif menu == "2": #선수 수정하는 부분
            name, choice, newinfo = ConsoleScreen.showPlayerUpdate()
            result = playerDAO.update(name, choice, newinfo)
            ConsoleScreen.showResult(result)            

        elif menu == "3": # 선수 삭제하는 부분
            player = ConsoleScreen.showPlayerDelete()
            result = playerDAO.delete(player)
            ConsoleScreen.showResult(result)


        elif menu == "4": # 선수 조회 부분
            searchTxt = ConsoleScreen.showSearchName()
            players = playerDAO.get(searchTxt)
            ConsoleScreen.showPlayer2(players)

        elif menu == "5": # 포지션 조회 부분
            searchTxt = ConsoleScreen.showSearchPosition()
            players = playerDAO.get2(searchTxt)
            ConsoleScreen.showPlayerPosition(players)

        elif menu == "6": #팀별 선수 조회 부분
            searchTxt = ConsoleScreen.showSearchTeam()
            players = playerDAO.get3(searchTxt)
            ConsoleScreen.showPlayerTeam(players)

        elif menu == "7": # 전체 선수 조회 부분
            players = playerDAO.getAll()
            ConsoleScreen.showPlayers(players)

        elif menu == "8": # 팀 등록 부분
            team = ConsoleScreen.showRegTeamMenu()
            result = teamDAO.reg(team)
            ConsoleScreen.showResult(result)

        elif menu == "9": #팀 수정 부분
            name, choice, newinfo = ConsoleScreen.showTeamUpdate()
            result = teamDAO.update(name, choice, newinfo)
            ConsoleScreen.showResult(result)            

        
        elif menu == "10": #팀 삭제 부분
            team = ConsoleScreen.showTeamDelete()
            result = teamDAO.delete(team)
            ConsoleScreen.showResult(result)

        elif menu == "11": #팀 조회 부분
            searchTxt = ConsoleScreen.showSearchTeam()
            teamAllName = teamDAO.getTeamName(teams)
            teams = teamDAO.getTeam(searchTxt)
            ConsoleScreen.showTeams(teams)
                
        elif menu == "12": # 전체 팀 조회 부분
            teams = teamDAO.getAll()
            ConsoleScreen.showTeams(teams)  