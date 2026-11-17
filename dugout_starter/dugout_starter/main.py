"""Session 2 checkpoint: Player and FantasyTeam, with one XI typed in by hand."""


class Player:
    """One real cricketer in the PSL player list."""

    def __init__(self, player_id, name, franchise, role, credits):
        self.player_id = player_id
        self.name = name
        self.franchise = franchise
        self.role = role
        self.credits = credits

    def __str__(self):
        return f"{self.name} ({self.franchise}, {self.role}, {self.credits} cr)"


class FantasyTeam:
    """A fantasy XI picked by one person."""

    def __init__(self, team_name, owner):
        self.team_name = team_name
        self.owner = owner
        self.players = []
        self.captain = None
        self.vice_captain = None

    def add_player(self, player):
        self.players.append(player)

    def total_credits(self):
        total = 0
        for player in self.players:
            total = total + player.credits
        return total

    def count_by_role(self):
        counts = {"WK": 0, "BAT": 0, "AR": 0, "BOWL": 0}
        for player in self.players:
            counts[player.role] = counts[player.role] + 1
        return counts

    def set_captain(self, captain, vice_captain):
        self.captain = captain
        self.vice_captain = vice_captain

    def __str__(self):
        size = len(self.players)
        cost = self.total_credits()
        return f"{self.team_name} (owner: {self.owner}, {size} players, {cost} cr)"


team = FantasyTeam("Dugout Demo XI", "Haroon")
mendis = Player("P086", "BKG Mendis", "Peshawar Zalmi", "WK", 8.0)
fakhar = Player("P056", "Fakhar Zaman", "Lahore Qalandars", "BAT", 8.5)
smith = Player("P075", "SPD Smith", "Multan Sultans", "BAT", 7.5)
nawaz = Player("P106", "Hassan Nawaz", "Quetta Gladiators", "BAT", 9.5)
shafique = Player("P054", "Abdullah Shafique", "Lahore Qalandars", "BAT", 8.5)
saim = Player("P012", "Saim Ayub", "Hyderabad Kingsmen", "AR", 10.5)
sams = Player("P064", "DR Sams", "Lahore Qalandars", "AR", 9.0)
hasan = Player("P046", "Hasan Ali", "Karachi Kings", "BOWL", 10.0)
joseph = Player("P113", "AS Joseph", "Quetta Gladiators", "BOWL", 9.5)
usama = Player("P070", "Usama Mir", "Lahore Qalandars", "BOWL", 9.5)
asif = Player("P133", "Asif Afridi", "Rawalpindiz", "BOWL", 6.5)

for player in [mendis, fakhar, smith, nawaz, shafique, saim, sams, hasan, joseph, usama, asif]:
    team.add_player(player)
team.set_captain(saim, hasan)

print(team)
print("Roles:", team.count_by_role())
print("Captain:", team.captain)
print("Vice-captain:", team.vice_captain)
