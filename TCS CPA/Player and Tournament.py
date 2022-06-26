# Author : Nanthakumar J J

# Profile : jjnanthakumar.github.io

__author__ = "https://jjnanthakumar.github.io"


class Player:
    def __init__(self, playerName, team, playerType, isCaptain, runs, wickets):
        self.playerName = playerName
        self.team = team
        self.playerType = playerType
        self.isCaptain = isCaptain.lower()=="true"
        self.runs = runs
        self.wickets = wickets

    def calculatePoints(self):
        fantasy_points = self.runs + (self.wickets*10)
        return fantasy_points*2 if self.isCaptain else fantasy_points


class Tournament:
    def __init__(self, playerList) -> None:
        self.playerList = playerList

    def getPlayerList(self, playerType, points):
        filtered = list(filter(lambda x: x.playerType.lower() == playerType.lower() and x.calculatePoints() > points, self.playerList))
        return filtered if filtered else None

    def findPlayerPoints(self, team, points):
        filteredPlayers = list(filter(lambda x: x.team.lower() == team.lower() and x.calculatePoints() > points, self.playerList))
        if not filteredPlayers:
            return None
        return {e.playerName: e.calculatePoints() for e in filteredPlayers}

if __name__ == "__main__":
    N = int(input())
    playerObjects = [Player(input(), input(),input(), input(),int(input()), int(input())) for _ in range(N)]
    tournament = Tournament(playerObjects)
    playerType, points1 = input(), int(input())
    team, points2 = input(), int(input())
    out1 = tournament.getPlayerList(playerType, points1)
    if out1 is None:
        print("Player Not Found.")
    else:
        for e in out1:
            print(e.playerName)
            print(e.runs)
            print(e.wickets)
    out2 = tournament.findPlayerPoints(team, points2)
    if out2 is None:
        print("Player Not Found.")
    else:
        print('\n'.join(f"{k} {v}" for k,v in out2.items()))
    

