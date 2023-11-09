class Mahasiswa:
    def __init__(self, nama, nim, jurusan, ipk):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    def hitung_predikat(self):
        if self.ipk >= 3.5:
            return "Cumlaude"
        elif self.ipk >=3.0:
            return "Sangat Memuaskan"
        elif self.ipk >=2.5:
            return "Memuaskan"
        elif self.ipk  >= 2.0:
            return "Cukup"
        elif self.ipk <= 2.0:
            return "Kurang"
        
    def info (self):
        predikat = self.hitung_predikat()
        print(f"Nama    : {self.nama}")
        print(f"NIM     : {self.nim}")
        print(f"Jurusan : {self.jurusan}")
        print(f"IPK     : {self.ipk}")
        print(f"Predikat: {predikat}")

mahasiswa1 = Mahasiswa("Naura", "H071231051", "Sistem Informasi", 3.98)
mahasiswa1.info()

    
