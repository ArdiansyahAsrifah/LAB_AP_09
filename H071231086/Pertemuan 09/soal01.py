class Human:
    def __init__(self, name, position):
        self.name = name
        self.__position = position  # Atribut position di-set sebagai private
        self._speed = 0  # Inisialisasi atribut speed

    def movement(self, direction):
        if direction == "L":
            self.__position -= self._speed
        elif direction == "R":
            self.__position += self._speed

    # Setter dan Getter untuk speed
    def set_speed(self, speed):
        self._speed = speed

    def get_speed(self):
        return self._speed

    def get_position(self):
        return self.__position


class Hero(Human):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power = 15
        self._health = 400
        self._armor = 15
        self.set_speed(3)

    def attack(self, target):
        target._health -= self._power  # Mengurangi health target langsung

    def get_health(self):
        return self._health

    def get_armor(self):
        return self._armor


class Warrior(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power = 25
        self._armor = 30

    def special(self, target):
        self._armor = 45
        self._power = 32
        target._health -= self._power  # Mengurangi health target langsung

    def get_power(self):
        return self._power

    def get_armor(self):
        return self._armor


class Assassin(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power = 35
        self.set_speed(4)

    def special(self, target):
        self.set_speed(7)
        self._power = 42
        target._health -= self._power  # Mengurangi health target langsung

    def get_speed(self):
        return self._speed


class Support(Human):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._health = 500
        self.set_speed(4)
        self._armor = 8

    def special(self, target):
        self.set_speed(6)
        target._health += 150  # Menambah health target langsung

    def get_health(self):
        return self._health

    def get_armor(self):
        return self._armor


# Contoh penggunaan:
warrior = Warrior("Bambang", position=10)
assassin = Assassin("Joko", position=25)
support = Support("Udin", position=30)

# Sebelum
print("Health (before):", warrior.get_health())
assassin.attack(warrior)
# Sesudah
print("Health (after):", warrior.get_health())
print("-" * 10)

# Sebelum
print("Warrior (health):", warrior.get_health())
print("Support (speed):", support.get_speed())
support.special(warrior)
# Sesudah
print("Warrior (health):", warrior.get_health())
print("Support (speed):", support.get_speed())
