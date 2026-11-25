from mahwish_dugout.errors import PlayerNotFoundError
from mahwish_dugout.errors import InvalidTeamError
from mahwish_dugout.loader import load_players, load_teams
from mahwish_dugout.models import find_player
 
players = load_players("data/players.csv")
#print(find_player(players, "Po89"))
#print(find_player(players, "P989"))
 
for team in load_teams("data/sample_teams.csv", players):
    try:
        team.validate()
        print(f"{team.team_name}: LEGAL")   
    except InvalidTeamError as error:
        print(f"{team.team_name}: {error}")

#raise PlayerNotFoundError("P999")