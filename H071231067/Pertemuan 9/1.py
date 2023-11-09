class Human:
    def __init__ (self,name,pos_x,speed = 1):
        self.name = name
        self.__position = pos_x
        self._speed = speed
    
    def movement(self,arah):
        for i in arah:
            if i == 'L':
                self.__position = self.__position - self._speed
            elif i == 'R':
                self.__position = self.__position+ self._speed
    
    def setPosition(self,pos_x):
        self.__position = pos_x
    def getPosition(self):
        return self.__position
    
class Hero(Human):
    def __init__ (self,name,pos_x):
        super().__init__(name,pos_x)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3
        
    def attack(self,target):
        target._health = target._health - self._power
        
    def setHealth(self,health):
        self._health = health
    def getHealth(self):
        return self._health
    
    def setSpeed(self,speed):
        self._speed = speed
    def getSpeed(self):
        return self._speed
    
    def setPower(self,power):
        self._power = power
    def getPower(self):
        return self._power
    
    def setArmor(self,armor):
        self._armor = armor
    def getArmor(self):
        return self._armor
    
    
class Warrior(Hero):
    def __init__ (self,name,pos_x):
        super().__init__(name,pos_x)
        self._power = 26
        self._armor = 30
    
    def special(self,target):
        print('Sedang menggunakan Special Skill')
        self._armor = 45
        self._power = 32
        target.setHealth(target.getHealth()-self._power)
        
        
class Assassin(Hero):
    def __init__ (self,name,pos_x):
        super().__init__(name,pos_x)
        self._power = 35
        self._speed = 4
    
    def special(self,target):
        print('Sedang menggunakan Special Skill')
        self._speed = 7
        self._power = 42
        target.setHealth(target.getHealth()-self._power)
        
        
class Support(Hero):
    def __init__ (self,name,pos_x):
        super().__init__(name,pos_x)
        self._health = 500
        self._armor = 8
        self._speed = 4
    
    def special(self,target):
        print('Sedang menggunakan Special Skill')
        self._speed = 6
        target.setHealth(target.getHealth() + 150)


warrior = Warrior("bambang", pos_x=10)
assassin = Assassin("joko", pos_x=25)
support = Support("udin",pos_x=30)

# sebelum
print("health (before) \t:", warrior.getHealth())
assassin.attack(warrior)
# sesudah
print("health (after) \t:", warrior.getHealth())
print("-"*10)
# sebelum
print("Warrior (health) \t:", warrior.getHealth())
print("Support (speed) \t: ",support.getSpeed())
support.special(warrior)
# sesudah
print("Warrior (health) \t:", warrior.getHealth())
print("Support (speed) \t: ",support.getSpeed())

# movement
print(f'posisi Warrior (before)\t: {warrior.getPosition()}')
warrior.movement('RRRRRRL')
print(f'Posisi Warrior (After) \t: {warrior.getPosition()}')
