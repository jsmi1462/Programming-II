class Inventory:
    def __init__(self, items=None):
        if items is None:
            items = []
        self.items = items
    def add_item(self, item):
        self.items.append(item)
        print(f"Added {item.name} to inventory.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Removed {item.name} from inventory.")
        else:
            print(f"{item.name} not found in inventory.")

    def display_inventory(self):
        if self.items:
            print("Inventory:")
            for item in self.items:
                print(f"- {item.name}")
        else:
            print("Inventory is empty.")

class Entity:
    def __init__(self, health, level, xp, size, race, strength, weight_limit):
        self.health = health
        self.level = level
        self.xp = xp
        self.size = size
        self.race = race
        self.strength = strength
        self.weight_limit = weight_limit
        self.inventory = Inventory()
        #self.items = Items()

    def level_up(self):
        requirement = 50 + (self.level * 2) 
        if self.xp >= requirement:
            self.level += 1
            print(f"{self.race} leveled up to {self.level}!")

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            print(f"The {self.race} died!")
        else:
            print(f"The {self.race} has {self.health} HP remaining.")

    def describe(self):
        return f"You see a {self.race} (Size: {self.size}, Str: {self.strength}, Lvl: {self.level}, HP: {self.health})"

    def attack(self, weapon, target):
        print(f"The {self.race} attacks the {target.race} with {weapon.name}!")
        total_damage = weapon.damage + self.strength
        target.take_damage(total_damage)
        weapon.degrade(self.inventory)

    def add_weapon_to_inventory(self, weapon):
        self.inventory.add_item(weapon)
        print(f"The {self.race} equips {weapon.name}.")

    def remove_weapon_from_inventory(self, weapon):
        self.inventory.remove_item(weapon)
        print(f"The {self.race} unequips {weapon.name}.")

class Weapon:
    def __init__(self, name, damage, durability, size, rarity, special):
        self.name = name
        self.damage = damage
        self.durability = durability
        self.size = size
        self.rarity = rarity
        self.special = special

    def degrade(self, inventory):
        if self.durability > 0:
            self.durability -= 1
            print(f"{self.name} durability: {self.durability}")
            if self.durability <= 0:
                print(f"{self.name} broke!")
                inventory.remove_item(self)

def main():
    # Entity: health, level, xp, size, race, strength
    hero = Entity(20, 1, 0, "large", "human", 2)
    nubian_goat = Entity(15, 1, 0, "tiny", "goat", 1)

    # Weapon: name, damage, durability, size, rarity, special
    kicking_boots = Weapon("kicking boots", 5, 10, "20.5", "mythical", "roundhouse")
    hooves = Weapon("hooves", 1, 15, "tiny", "common", "ram")

    print(f"Behold your mighty hero!!! {hero.describe()}")
    print(f"{nubian_goat.describe()}")

    # Equip weapons
    hero.add_weapon_to_inventory(kicking_boots)
    nubian_goat.add_weapon_to_inventory(hooves)

    # Display inventory
    hero.inventory.display_inventory()
    nubian_goat.inventory.display_inventory()

    # New logic: Entity.attack(weapon, target)
    nubian_goat.attack(hooves, hero)

    # Display inventory after attack
    nubian_goat.inventory.display_inventory()

if __name__ == "__main__":
    main()
