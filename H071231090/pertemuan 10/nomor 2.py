from abc import ABC, abstractmethod

# Abstract class
class kendaraan(ABC):
    def __init__(self, brand, model):
        self._brand = brand
        self._model = model

    @abstractmethod
    def setir(self):
        pass

    def get_info(self):
        return f"{self._brand} {self._model}"


# Inheritance
class Mobil(kendaraan):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    # Polymorphism
    def setir(self):
        return f"{self.get_info()} sedang dikendarai di jalan."


class Motor(kendaraan):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    # Polymorphism
    def setir(self):
        return f"{self.get_info()} sedang dikendarai di jalan."


class Truk(kendaraan):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    # Polymorphism
    def setir(self):
        return f"{self.get_info()} sedang mengangkut barang di jalan."


# Encapsulation
class Pergi:
    def __init__(self):
        self._kendaraan = []

    def add_kendaraan(self, kendaraan):
        self._kendaraan.append(kendaraan)

    def loop_kendaraan(self):
        for i in self._kendaraan:
            print(i.setir())


# penggunaan
car = Mobil("Toyota", "Corolla")
motorcycle = Motor("Harley-Davidson", "Street 750")
truck = Truk("Volvo", "VNL 760")

x = Pergi()
x.add_kendaraan(car)
x.add_kendaraan(motorcycle)
x.add_kendaraan(truck)

x.loop_kendaraan()