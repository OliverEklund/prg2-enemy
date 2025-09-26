player = {"attack" : 5}

class Enemy:
    def __init__(self, health: int, attack: int, name: str):
        self.health = health
        self.attack = attack
        self.name = name
    
    def print_attack(self):
        print(f"{self.name} attackerar dig och gör {self.attack} skada")
    
    def take_damage(self):
        self.health -= player['attack']
        print(f"{self.name} tar {player['attack']} i skada och {self.health} hälsa kvar.")



    def print_status(self):
        print(f"En {self.name} står framför dig och har {self.health} hälsa och {self.attack} attack.")

vätte = Enemy(10, 5, "Vätte")
vätte.print_status()
vätte.print_attack()
vätte.take_damage()