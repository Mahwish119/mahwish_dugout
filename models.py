class Player:
    #constructor 
    def __init__(self, player_id, name, role, franchise, credits):
        self.player_id = player_id
        self.name = name 
        self.role = role 
        self.franchise = franchise
        self.credits = credits

    @classmethod
    #"""decorator to create a Player object from a row of data"""
    def from_row(cls, row):
        return cls(
            row["player_id"],
            row["name"],
            row["role"],
            row["franchise"],
            row["credits"]
        )

    def __str__(self):
        return f"{self.name} ({self.franchise}, {self.role}, {self.credits} cr)"


class FantacyTeam:
    """A fantacy XI picked by one person"""
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
            total += player.credits 
        return total

    def count_by_role(self):
        counts = {'Wicket Keeper': 0, 'Batter': 0, 'All Rounder': 0, 'Bowler': 0} 
        for player in self.players:
            counts[player.role] = counts[player.role] + 1
        return counts

    def set_captain(self, captain, vice_captain):
        self.captain = captain
        self.vice_captain = vice_captain

    def count_by_franchise(self):
        """return a dictionary of franchise -> number of players from that franchise"""
        counts = {}
        for player in self.players:
            #get(key,0)gives 0 the first time we see a franchise
            counts[player.franchise] = counts.get(player.franchise, 0) +1
            return counts

    def __str__(self):
        size = len(self.players)
        cost = self.total_credits()
        return f"{self.team_name} (owner:{self.owner},{size} players, {cost} cr)"



babar = Player("P089", "Babar Azam", "Batter", "Peshawer Zalmi", 10.5)
usman = Player("P002", "Usman Khan", "Wicket Keeper", "Hyderabad Kingsmen", 10.5 )
irfan = Player("P004", "Irfan Khan", "Batter", "Hyderabad Kingsmen", 6.5)
imad = Player ("P028", "Imad Wasim", "All Rounder", "Islamabad United", 9.5)
shadab = Player("P029", "Shadab Khan", "All Rounder", "Islamabad United", 9.5)
gleeson = Player("P032", "R J Gleeson", "Bowler", "Islamabad United", 7.5)
amir = Player("P137", "Mohammad Amir", "Bowler", "Rawalpindi", 8.7)
nawaz = Player("P106", "Hassan Nawaz", "Batter", "Quetta Gladiator", 9.5)
mg = Player("P107", "MG Bracewell", "All Rounder", "Peshawer Zalmi", 8.0)
shan= Player("P076", "Shan Masood", "Batter", "Karachi Kings", 6.0)
hasnain = Player("P031", "Mohammad Hasnain", "Bowler", "Islamabad United", 6.0)

team = FantacyTeam("Kings XI", "Mahwish")
team.add_player(babar)
team.add_player(usman)
team.add_player(irfan)
team.add_player(imad)
team.add_player(shadab)
team.add_player(gleeson)
team.add_player(amir)
team.add_player(nawaz)
team.add_player(mg)
team.add_player(shan)
team.add_player(hasnain)

team.set_captain(shadab, usman)

print(team)
print(f"Roles  : {team.count_by_role()}")
print(f"captain :   {team.captain}")
print(f"vice-captain :  {team.vice_captain}")

for player in team.players:
    print(player)
