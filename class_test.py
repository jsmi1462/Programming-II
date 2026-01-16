class Enemy:
    def __init__(self, race, hp, size, damage, description):
        self.hp = hp
        self.size = size
        self.damage = damage
        self.description = description
        self.race = race
    
    def describe(self):
        return f"{self.description} {self.race} that is {self.size} that has {self.hp} hit points and can do {self.damage} damage per hit"
    
troll = Enemy("troll", 50, "Large", 10, "ugly, warty, and stinky")
print(f"You encounter a {troll.describe()}!")