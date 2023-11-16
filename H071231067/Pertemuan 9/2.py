class Mahasiswa:
    def __init__ (self,nama,nim,jurusan,ipk):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk
    
    def tampilkan_info(self):
        print(f'Nama    : {self.nama}')
        print(f'NIM     : {self.nim}')
        print(f'Jurusan : {self.jurusan}')
        print(f'IPK     : {self.ipk}')
    
    def hitung_predikat(self):
        if self.ipk >= 3.5:
            print('Cumlaude')
        elif self.ipk >= 3.0:
            print('Sangat Memuaskan')
        elif self.ipk >= 2.5:
            print('Memuaskan')
        elif self.ipk >= 2.0:
            print('Cukup')
        elif self.ipk < 2.0:
            print('Kurang')

def input_ipk():
    while True:
        try:
            ipk = float(input('Masukkan IPK \t: '))
            if ipk >= 0.0 and ipk <= 4.0:
                return ipk
            else:
                print('IPK tidak valid (0-4)')
        except ValueError:
            print('IPK tidak valid (0-4)')
            
mahasiswa = Mahasiswa(
    nama = input('Masukkan Nama \t: '),
    nim = input('Masukkan NIM \t: '),
    jurusan = input('Masukkan Jurusan: '),
    ipk = input_ipk()
)
print('='*50)
print('1. Tampilkan Info Mahasiswa')
print('2. Hitung Predikat')
print('3. Keluar')
print('='*50)

while True:
    opsi = input('Masukkan opsi \t: ')
    print('='*50)
    if opsi == '1':
        mahasiswa.tampilkan_info()
        print('='*50)
    elif opsi == '2':
        mahasiswa.hitung_predikat()
        print('='*50)
    elif opsi == '3':
        break
    else:
        print('Pilih 1 sampai 3')
        print('='*50)