
from mahwish_dugout.loader import load_players, load_teams, load_team
from mahwish_dugout.loader import team_from_row
from mahwish_dugout.errors import InvalidTeamError, PlayerNotFoundError


from mahwish_dugout.loader import (
    load_players,
    load_team,
    load_teams,
    read_team_rows,
    team_from_row,
)

 
 
def show_pool(players):
    """Print how many players there are per franchise and per role."""
 
    by_franchise = {}
    by_role = {}
 
    for player in players.values():
        # .get(key, 0) gives 0 the first time we see a key, then we add 1
        by_franchise[player.franchise] = by_franchise.get(player.franchise, 0) + 1
        by_role[player.role] = by_role.get(player.role, 0) + 1
 
    print("Players by franchise:")
    for franchise in sorted(by_franchise):
        print(f"  {franchise}: {by_franchise[franchise]}")
 
    print("Players by role:")
    for role in sorted(by_role):
        print(f"  {role}: {by_role[role]}")

def show_team(team):
    """print a team's players, cost and captains."""
    print(f"\n Team {team.team_name }  by  {team.owner}: ")
    for player in team.players:
        print(f"   {player}")
    print (f"total credits: {team.total_credits()}")
    print(f"Captain:  {team.captain.name}, Vice-captain:  {team.vice_captain.name }")

def report(team_name, problems):
    """Print one verdict. An empty list of problems means the team is legal."""
 
    if not problems:
        print(f"  {team_name}: LEGAL")
        return
 
    print(f"  {team_name}: REJECTED")
    for problem in problems:
        print(f"    - {problem}")
 
 
def report_on_row(row, players):
    """Build one team from a CSV row and say whether it is legal. 
    Both things that can be wrong are caught here, so one bad team never stops the rest of the file. """
 
    try:
        team = team_from_row(row, players)
        team.validate()
    except PlayerNotFoundError as error:
        report(row["team_name"], [str(error)])
    except InvalidTeamError as error:
        report(error.team_name, error.problems)
    else:
        report(team.team_name, [])




def main():
    players = load_players("data\\players.csv")
    show_pool(players)
    my_team = load_team("data\\my_team.csv", players)
    show_team(my_team)
    print("\nMy team")
    report(my_team.team_name, my_team.check_rules())

    print("The six sample teams from week 1")
    for team in load_teams("data\\sample_teams.csv", players):
        report(team.team_name, team.check_rules())

    print("the six teams the legal office could not accept")
    for row in read_team_rows("data\\bad_teams.csv"):
        report_on_row(row,players)

    print("\n Done. Six team were refused and the program did not crash. ")

    #team = load_teams("data\\sample_teams.csv", players)

    # legal = []
    # illegal = []
 
    # for team in teams:
    #     show_team(team)
 
    #     errors = team.check_rules()
    #     if errors:
    #         illegal.append(team)
    #         print("ILLEGAL:")
    #         for error in errors:
    #             print(f"  - {error}")
    #     else:
    #         legal.append(team)
    #         print("LEGAL")
 
    # print(f"\nSummary: {len(legal)} legal, {len(illegal)} illegal out of {len(teams)} teams")
 
    # print("Legal teams:")
    # for team in legal:
    #     print(f"  {team.team_name}")
 
    # print("Illegal teams:")
    # for team in illegal:
    #     print(f"  {team.team_name}")
 

 
 

# Only run when this file is executed directly, not when it is imported
if __name__ == "__main__":
    main()