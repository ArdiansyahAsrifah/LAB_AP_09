class Human :
    def __init__(self, name, position):
        self.name = name
        self._speed = 0
        self.__position = position

    def movement(self, direct):
        if direct.upper() == "L":
            self.__position -= self._speed
            print(f"{self.name.title()} moved, now {self.name.title()} was on {self.__position}")
        elif direct.upper() == "R":
            self.__position += self._speed
            print(f"{self.name.title()} moved, now {self.name.title()} was on {self.__position}")
        else:
            print("Direction has not descriptable, please choose L/R !")
    
    def set_position(self, position):
        self.__position = position
    
    def get_position(self):
        return self.__position
    
class Hero(Human):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.set_position(position)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3
    def attack(self, target):
        target._health -= self._power
        print(f"{self.name.title()} attacked {target.name.title()} deals {self._power} damage, {target.name.title()} health {target._health} left")

    def set_power(self, power):
        self._power = power

    def get_power(self):
        return self._power
    
    def set_health(self, health):
        self._health = health

    def get_health(self):
        return self._health
    
    def set_speed(self, speed):
        self._speed = speed

    def get_speed(self):
        return self._speed
    
    def set_armor(self, armor):
        self._armor = armor

    def get_armor(self):
        return self._armor
    
class Warrior(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.set_position(position)
        self._power = 26
        self._armor = 30
        
    def special(self, target):
        self._armor = 45
        self._power = 32
        target._health -= self._power
        print(f"{self.name.title()} use special skill and deals {self._power} damage! {target.name.title()} health {target._health} left")

class Assassin(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.set_position(position)
        self._power = 35
        self._speed = 4

    def special(self, target):
        self._armor = 42
        self._power = 7
        target._health -= self._power
        print(f"{self.name.title()} use special skill and deals {self._power} damage! {target.name.title()} health {target._health} left")

class Support(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.set_position(position)
        self._health = 500
        self._armor = 8
        self._speed = 4
        self._healing = 150

    def special(self, target):
        self._speed = 6
        target._health += self._healing
        print(f"{self.name.title()} use special skill and heal {self._healing} health! {target.name.title()} health now is {target._health}")
    
assassin = Assassin("ninja", 80)
warrior = Warrior("bambang", 10)
assassin = Assassin("joko",  25)
support = Support("udin",    30)
# sebelum
print("health (before)", warrior.get_health())
assassin.attack(warrior)
# sesudah
print("health (after)", warrior.get_health())
print("-"*10)
# sebelum
print("warrior (health)", warrior.get_health())
print("support (speed) : ",support.get_speed())
print("-"*10)
support.special(warrior)
# sesudah
print("Warrior (health)", warrior.get_health())
print("support (speed): ",support.get_speed())

# warrior.special(assassin)
# assassin.special(warrior)
# print(assassin._speed)
# assassin.movement("r")
# warrior.attack(assassin)
# support.special(assassin)
# assassin.special(warrior)
# assassin.special(warrior)
# assassin.special(warrior)
# print(assassin._dict_)
# print(assassin.set_position(19))

# assassin.movement("L")
# print(warrior.get_position())