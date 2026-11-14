class Player:
    #constructor 
    def __init__(self, player_id, name, role, franchise, credits):
        self.player_id = player_id
        self.name = name 
        self.role = role 
        self.franchise = franchise
        self.credits = credits

    def __str__(self):
        return f"{self.name} ({self.franchise}, {self.role}, {self.credits} cr)"
    

#object 
babar = Player("P089", "Babar Azam", "Batter", "Peshawer Zalmi", 10.5)
usman = Player("P002", "Usman Khan", "Wicket Keeper", "Hyderabad Kingsmen", 10.5 )
irfan = Player("P004", "Irfan Khan", "Batter", "Hyderabad Kingsmen", 6.5)
imad = Player ("P028", "Imad Wasim", "All Rounder", "Islamabad United", 9.5)
shadab = Player("P029", "Shadab Khan", "All Rounder", "Islamabad United", 9.5)

for player in [babar, usman, irfan, imad, shadab]:
    print(player)
