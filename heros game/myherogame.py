import random

class Weapon:
    def __init__(self, name):
        self.name = name

class Sword(Weapon):
    def __init__(self):
        super().__init__("Mač")

class Spear(Weapon):
    def __init__(self):
        super().__init__("Koplje")

class Spell(Weapon):
    def __init__(self):
        super().__init__("Čarolija")

class NoWeapon(Exception):
    pass

class Hero:
    def __init__(self, name, health, weapon=None):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.weapons = []

    def add_weapon(self, weapon):
        if len(self.weapons) == 2:
            raise Exception("Maksimalan broj oružja u rancu je 2.")
        self.weapons.append(weapon)

    def drop_weapon(self, index):
        if not self.weapons:
            raise NoWeapon("Torba je prazna.")
        weapon = self.weapons.pop(index)
        if self.weapon == weapon:
            self.weapon = None
        return weapon

    def change_weapon(self, index):
        if not self.weapons:
            raise NoWeapon("Torba je prazna.")
        self.weapon = self.weapons[index]

    def attack(self, monster):
        if isinstance(self.weapon, Sword):
            damage = 10
        elif isinstance(self.weapon, Spear):
            damage = 15
        elif isinstance(self.weapon, Spell):
            damage = 20
        else:
            raise NoWeapon("Heroj nema oružje.")
        monster.health -= damage
        print(f"{self.name} je napao {monster.name} pomoću {self.weapon.name}.")

class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, hero):
        attack_type = random.choice(["Udara", "Bljuje vatru", "Ujeda"])
        if isinstance(self, Dragon):
            if attack_type == "Udara":
                damage = 5
            else:
                damage = 20
        elif isinstance(self, Spider):
            if attack_type == "Udara":
                damage = 5
            else:
                damage = 8
        hero.health -= damage
        print(f"{self.name} je napao {hero.name} pomoću {attack_type}.")

class Dragon(Monster):
    def __init__(self, name="Zmaj", health=100):
        super().__init__(name, health)

class Spider(Monster):
    def __init__(self, name="Pauk", health=50):
        super().__init__(name, health)

def simulate_battle(hero, monster):
    while hero.health > 0 and monster.health > 0:
        if random.randint(0, 100) < 50:
            hero.attack(monster)
        else:
            monster.attack(hero)
    if hero.health > 0:
        return hero
    else:
        return monster

def simulate_tournament(heroes, monsters):
    winners = []
    for i in range(0, len(heroes), 2):
        winner = simulate_battle(heroes[i], heroes[i+1])
        winners.append(winner)
    for i in range(0, len(winners), 2):
        winner = simulate_battle(winners[i], winners[i+1])
        winners[i] = winner
    return winners[0]

# Testiranje
hero1 = Hero("Čarobnjak", 150)
hero1.add_weapon(Spell())
hero1.add_weapon(Sword())
hero1.change_weapon(0)

hero2 = Hero("Mačevalac", 100)
hero2.add_weapon(Sword())
hero2.add_weapon(Spear())
hero2.change_weapon(0)

dragon = Dragon()
spider = Spider()

winner1 = simulate_battle(hero1, dragon)
winner2 = simulate_battle(hero2, spider)
final_winner = simulate_battle(winner1, winner2)

print(f"{winner1.name} je pobedio u duelu sa {dragon.name}.")
print(f"{winner2.name} je pobedio u duelu sa {spider.name}.")
print(f"{final_winner.name} je pobedio u finalu i postao šampion!")
