# Base Class
class Hero :
    def __init__ (self,nama,role):
        self.__nama = nama # encapsulation
        self.__role = role

    def show_info(self):
        pass
    
    def setNama(self,nama):
        self.__nama = nama
    def getNama(self):
        return self.__nama
    def setRole(self, role):
        self.__role = role
    def getRole(self):
        return self.__role

# Derived class (inheritance)
class Tank(Hero):
    def __init__(self, nama):
        super().__init__(nama, "Tank")
    def show_info(self):
        print(f"Nama: {self.getNama()}, Role: {self.getRole()}")

class Assasin(Hero):
    def __init__(self, nama):
        super().__init__(nama, "Assasin")
    def show_info(self):
        print(f"Nama: {self.getNama()}, Role: {self.getRole()}")

class Fighter(Hero):
    def __init__(self, nama):
        super().__init__(nama, "Fighter")
    def show_info(self):
        print(f"Nama: {self.getNama()}, Role: {self.getRole()}")

class Marksman(Hero):
    def __init__(self, nama):
        super().__init__(nama, "Marksman")
    def show_info(self):
        print(f"Nama: {self.getNama()}, Role: {self.getRole()}")

class Mage(Hero):
    def __init__(self, nama):
        super().__init__(nama, "Mage")
    def show_info(self):
        print(f"Nama: {self.getNama()}, Role: {self.getRole()}")

class Support(Hero):
    def __init__(self, nama):
        super().__init__(nama, "Support")
    def show_info(self):
        print(f"Nama: {self.getNama()}, Role: {self.getRole()}")

# Instantiate objects
tank = Tank("Atlas")
assasin = Assasin("Ling")
fighter = Fighter("Roger")
marksman = Marksman("Claude")
mage = Mage("Odette")
support = Support("Angela")

#Polymorphism in action
tank.show_info()
print("-"*30)
assasin.show_info()
print("-"*30)
fighter.show_info()
print("-"*30)
marksman.show_info()
print("-"*30)
mage.show_info()
print("-"*30)
support.show_info()
print("-"*30)