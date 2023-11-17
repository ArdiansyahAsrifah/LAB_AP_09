class Bentuk:
    def __init__(self, nama):
        self.nama = nama

    def menghitung_luas(self):
        pass

class Bulat(Bentuk):
    def __init__(self, nama, radius):
        super().__init__(nama)
        self._radius = radius

    def menghitung_luas(self):
        return 3.14 * self._radius **2

    def getradius(self):
        return self._radius
    
    def set_radius(self, radius):
        self._radius = radius

class Segitiga(Bentuk):
    def __init__(self, nama, alas, tinggi):
        super().__init__(nama)
        self._alas = alas
        self._tinggi = tinggi

    def menghitung_luas(self):
        return 1/2 * self._alas * self._tinggi
    
    def getalas(self):
        return self._alas
    
    def set_alas(self, alas):
        self._alas = alas
    
    def gettinggi(self):
        return self._tinggi
    
    def set_tinggi(self, tinggi):
        self._tinggi = tinggi

bulat = Bulat("Lingkaran", 5)
segi_tiga = Segitiga("Segitigai", 4, 5)

bentuk = [bulat, segi_tiga]
for i in bentuk:
    print(f"Nama: {i.nama}, Luas: {i.menghitung_luas()}")