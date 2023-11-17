class Mahasiswa:
    def __init__(self, nama, nim, jurusan, IPK):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = IPK
    
    def Tampilkan_info(self):
        print(f"Nama\t: {self.nama}\nNIM\t: {self.nim}\nJurusan\t: {self.jurusan}\nIPK\t: {self.ipk}")
    
    def Hitung_predikat(self):
        nilai = self.ipk
        predikat = ""
        if nilai < 2 :
            predikat += "Kurang"
        elif nilai < 2.5 :
            predikat += "Cukup"
        elif nilai < 3.0 :
            predikat += "Memuaskan"
        elif nilai < 3.5 :
            predikat += "Sangat memuaskan"
        elif nilai <= 4.0 :
            predikat += "Cumlaude"
        elif nilai < 0 or nilai > 4:
            predikat += "Input Salah! IPK hanya dalam rentan 0-4 !!!"
        print(f"Predikat:{predikat}")

saya = Mahasiswa("Athifah Nur Rahman", "H071231016", "Sistem Informasi", 4.0)
saya.Tampilkan_info()
saya.Hitung_predikat()