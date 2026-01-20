class Enemy:
    def __init__(self, race, hp, size, damage, description):
        self.hp = hp
        self.size = size
        self.damage = damage
        self.description = description
        self.race = race
    
    def describe(self):
        return f"{self.description} {self.race} that is {self.size} that has {self.hp} hit points and can do {self.damage} damage per hit"
    
    def died(self):
        return "You killed the enemy"
    
troll = Enemy("troll", 50, "Large", 10, "ugly, warty, and stinky")
print(f"You encounter a {troll.describe()}!")

class Weapon:
    def __init__(self, damage, name, type, durability):
        self.damage = damage
        self.name = name
        self.type = type
        self.durability = durability
    
    def attack(self, damage, durability, name):
        durability = 10
        return f"{name} did {damage} and has {durability} remaining"

blunderbuss = Weapon(100, "blunderbuss", "gun", 10)
NissanAltima = Weapon(20000, "Nissan Altima", "car", 1)
print(f"You hit the {troll.race} with the {NissanAltima.name} and did {NissanAltima.damage} damage. {troll.race} has 0 hp left")
print(troll.died())
