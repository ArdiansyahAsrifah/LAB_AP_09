class Mahasiswa:
    def __init__(self, nama, nim, jurusan, ipk):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    def tampilkan_info(self):
        print("Informasi Mahasiswa:")
        print("Nama      : " + self.nama)
        print("NIM       : " + self.nim)
        print("Jurusan   : " + self.jurusan)
        print("IPK       : " + str(float(self.ipk)))

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
        print("Predikat  : " + predikat)
        print("="*50)

nama = input("Masukkan Nama Mahasiswa: ")
nim = input("Masukkan NIM Mahasiswa: ")
jurusan = input("Masukkan Jurusan Mahasiswa: ")
ipk = float(input("Masukkan IPK Mahasiswa: "))
print("="*50)
#object
mahasiswa1 = Mahasiswa (nama, nim, jurusan, ipk)

mahasiswa1.tampilkan_info()
mahasiswa1.hitung_predikat()