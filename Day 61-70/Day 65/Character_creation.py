class character:
    '''base class'''
    name = None
    health = None
    magic_points = None

    def __init__(self, name: str, health: int, magic_points: int):
        self.name = name
        self.health = health
        self.magic_points = magic_points

    def stats(self):
        '''output von stats'''
        print()
        print(f"Name:         \t{self.name:<10}")
        print(f"Health:       \t{self.health:<10}")
        print(f"Magic Points: \t{self.magic_points:<10}")


class player(character):
    lives = None
    player = None
    
    def __init__(self, name: str, health: int, magic_points: int, lives: int):
        super().__init__(name, health, magic_points)
        self.lives = lives
        self.player = "Player"
    
    def alive(self):
        if self.lives > 0:
            return "Alive"
        else:
            return "Dead"
    
    def stats(self):
        print()
        print(f"{self.player}")
        super().stats()
        print(f"Lives:        \t{self.lives:<10}")
        print(f"Alive?:       \t{self.alive():<10}")


class enemy(character):
    strength=None
    type_ = None
    
    def __init__(self, name: str, health: int, magic_points: int, strength: int, type_: str):
        super().__init__(name, health, magic_points)
        self.type_ = type_
        self.strength = strength
    
    def stats(self):
        print()
        super().stats()
        print(f"Type:         \t{self.type_:<10}")
        print(f"Strength:     \t{self.strength:<10}")


class orc(enemy):
    speed = None
    
    def __init__(self, name: str, health: int, magic_points: int, strength: int, speed: int):
        super().__init__(name, health, magic_points, strength, "Orc")
        self.speed = speed
    
    def stats(self):
        super().stats()
        print(f"Speed:        \t{self.speed:<10}")


class vampire(enemy):
    day=None

    def __init__(self, name: str, health: int, magic_points: int, strength: int, day: bool):
        super().__init__(name, health, magic_points, strength, "Vampire")
        self.day = "Day" if day else "Night"
    
    def stats(self):
        super().stats()
        print(f"Day/Night:    \t{self.day:<10}")


player = player("David", 100, 20, 1)
player.stats()

orc1 = orc("Gustav", 14, 2, 20, 20)
orc1.stats()

vamp1 = vampire("Alucard", 100, 250, 50, False)
vamp1.stats()
