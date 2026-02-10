class Entity:
    def __init__(self, name, hp, size, damage, description):
        self.hp = hp
        self.size = size
        self.damage = damage
        self.description = description
        self.name = name
    
    def describe(self):
        return f"{self.description} {self.race} that is {self.size} that has {self.hp} hit points and can do {self.damage} damage per hit"
    
    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            return f"{self.name} has died!"
        else:
            return f"{self.name} has {self.hp} remaining"


class Weapon:
    def __init__(self, damage, name, type, durability):
        self.damage = damage
        self.name = name
        self.type = type
        self.durability = durability
    
    def attack(self, enemy):
        if self.durability >= 1:
            self.durability -= 1
        else:
            #don't forget to remove the item from inventory!
            return f"{self.name} broke!"



def main():
    inventory = [blunderbuss, NissanAltima]
    troll = Entity("troll", 50, "Large", 10, "ugly, warty, and stinky")
    blunderbuss = Weapon(100, "blunderbuss", "gun", 10)
    NissanAltima = Weapon(20000, "Nissan Altima", "car", 1)

if __name__ == "__main__":
    main()
