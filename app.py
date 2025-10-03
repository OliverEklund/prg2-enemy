player = {"attack" : 5}

class Enemy:
    def __init__(self, health: int, attack: int, name: str):
        self.health = health
        self.attack = attack
        self.name = name
    
    def attack(self, target):
        print(f"{self.name} attackerar {target.name}")
        target.take_damage(self.attack)

    
    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} tar {damage} i skada och {self.health} hälsa kvar.")

    def print_status(self):
        print(f"{self.name} står framför dig och har {self.health} hälsa och {self.attack} attack.")

creature_1 = Enemy(10, 5, "Vätte")
creature_2 = Enemy(25, 8, "Troll")

creature_1.print_status()
creature_2.print_status()

creature_1.attack(creature_2.)
creature_2.take_damage(creature_1.attack)
creature_2.print_status()
