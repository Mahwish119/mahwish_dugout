class Player:
    #constructor 
    def __init__(self, player_id, name, role, franchise, credits):
        self.player_id = player_id
        self.name = name 
        self.role = role 
        self.franchise = franchise
        self.credits = credits

    def __str__(self):
        return(
            f"player Id : {self.player_id}\n",
            f"Name : {self.name}\n",
            f""
        )

#object 
babar = Player("P089", "Babar Azam", "Batter", "Peshawer Zalmi", 10.5)

print(babar.name)
print(babar.franchise)
print(babar.credits)

    