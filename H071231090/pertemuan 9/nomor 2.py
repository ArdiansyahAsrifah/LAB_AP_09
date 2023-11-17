class Mahasiswa:
    def __init__(self, nama, nim, jurusan, ipk):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    def tampilkan_info(self):
        print(f"Nama     : {self.nama}")
        print(f"NIM      : {self.nim}")
        print(f"Jurusan  : {self.jurusan}")
        print(f"IPK      : {self.ipk}")

    def hitung_predikat(self):
        if self.ipk >= 3.5:
            predikat = "Cumlaude"
        elif self.ipk >= 3.0:
            predikat = "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            predikat = "Memuaskan"
        elif self.ipk >= 2.0:
            predikat = "Cukup"
        else:
            predikat = "Kurang"
        return predikat
    
    
input = Mahasiswa("Fatimah", "H071231087", "Sistem Informasi", 3.8)
input.tampilkan_info()
predikat_mahasiswa1 = input.hitung_predikat()
print(f"Predikat : {predikat_mahasiswa1}")