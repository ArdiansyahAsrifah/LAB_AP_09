from abc import ABC, abstractmethod

class Hewan(ABC):
    def __init__(self, nama):
        self._nama = nama

    @property
    def nama(self):
        return self._nama

    @abstractmethod
    def suara(self):
        pass

class Anjing(Hewan):
    def suara(self):
        return "Woof!"

class Kucing(Hewan):
    def suara(self):
        return "Meow!"

def suara_hewan(hewan):
    return hewan.suara()

class KebunBinatang:
    def __init__(self):
        self._hewan = []

    def tambah_hewan(self, hewan):
        if isinstance(hewan, Hewan):
            self._hewan.append(hewan)
            print(f"{hewan.nama} ditambahkan ke kebun binatang.")
        else:
            print("Tipe hewan tidak valid.")

    def buat_semua_suara(self):
        for hewan in self._hewan:
            print(suara_hewan(hewan))

if __name__ == "__main__":
    anjing = Anjing("Buddy")
    kucing = Kucing("Whiskers")

    kebun_binatang = KebunBinatang()
    kebun_binatang.tambah_hewan(anjing)
    kebun_binatang.tambah_hewan(kucing)

    kebun_binatang.buat_semua_suara()
