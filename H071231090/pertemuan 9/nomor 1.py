class Human:
    def __init__(self, name, position):
        self.name = name
        self.__position = position
        self._speed = 0

    def getPosition(self):
        return self.__position

    def setPosition(self, position):
        self.__position = position

    def movement(self, direction):
        if direction == "L":
            self.setSpeed(self.getSpeed() - self._speed)
        elif direction == "R":
            self.setSpeed(self.getSpeed() + self._speed)


class Hero(Human):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3

    def getPower(self):
        return self._power

    def setPower(self, power):
        self._power = power

    def getHealth(self):
        return self._health

    def setHealth(self, health):
        self._health = health

    def getArmor(self):
        return self._armor

    def setArmor(self, armor):
        self._armor = armor

    def getSpeed(self):
        return self._speed

    def setSpeed(self, speed):
        self._speed = speed
    def attack(self, target):
        target.setHealth(target.getHealth() - self._power)


class Warrior(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._Armor = 30
        self._Power = 26

    def special(self, target):
        target.setPower(32)
        target.setArmor(45)
        target.setHealth(target.getHealth() - self.getPower())


class Assassin(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._Speed = 4        
        self._Power = 35

    def special(self, target):
        target.setHealth(target.getHealth() - self.getPower())
        target.setPower(42)
        target.Speed = 7


class Support(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._Health = 500
        self._Armor = 8
        self.speed = 4

    def special(self, target):
        self.speed = 6
        target.setHealth(target.getHealth() + 150)

warrior = Warrior("bambang", position = 10)
assassin = Assassin("joko", position = 25)
support = Support("udin", position = 30)

# Sebelum
print("health (before)", warrior.getHealth())
assassin.attack(warrior)

# Sesudah
print("health (after)", warrior.getHealth())
print("-" * 10)

# Sebelum
print("Warrior (health)", warrior.getHealth())
print("Support (speed):", support.speed)
support.special(warrior)

# Sesudah
print("Warrior (health)", warrior.getHealth())
print("Support (speed):", support.speed)