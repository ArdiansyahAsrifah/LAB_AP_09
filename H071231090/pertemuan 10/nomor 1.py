import re


class UserData:
    def __init__(self):
        self.nama = ""
        self.email = ""
        self.password = ""

    def detail_pribadi(self):
        if not self.nama:
            print("="*50)
            print("Data saat ini kosong")
        else:
            print("="*50)
            print("Data anda adalah")
            print(f"{'Nama':<20}: {self.nama}")
            print(f"{'Email':<20}: {self.email}")
            print(f"{'Password':<20}: {self.password}")

    def ubah_nama(self):
        if not self.nama:
            print("="*50)
            print("Data saat ini kosong")
        else:
            print("="*50)
            new_nama = input("Masukkan nama baru: ")
            self.nama = new_nama
            print("="*50)
            print("Nama berhasil diubah")

    def buat_data_baru(self):
        while True:
            print("="*50)
            nama = input("Masukkan Nama: ")

            # Email
            while True:
                email = input("Masukkan Email: ")
                email_pattern = re.compile(r"[a-z0-9._%+-]+@student.unhas.ac.id$")
                if not email_pattern.match(email):
                    print("="*50)
                    print("Email yang Anda Masukkan Salah")
                else:
                    break 

            # Password
            while True:
                password = input("Masukkan Password: ")
                if not (8 <= len(password) <= 20):
                    print("="*50)
                    print("Password harus memiliki Panjang 8-20 karakter")
                elif not (any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password)):
                    print("="*50)
                    print("Password yang Anda masukkan terlalu lemah, gunakan minimal 1 huruf kapital, huruf kecil, dan angka")
                else:
                    break  

            # simpan data
            self.nama = nama
            self.email = email
            self.password = password
            print("="*50)
            print("Data berhasil disimpan")
            break 


class MainMenu:
    def __init__(self):
        self.file = ""
        self.file_name = ""
        self.user_data = UserData()

    def start(self):
        self.file = ""
        self.file_name = ""
        self.menu()

    def menu(self):
        while True:
            print("="*50)
            print("Selamat datang, Silakan Pilih Opsi Menu")
            print("1. Detail Anda")
            print("2. Ubah Nama")
            print("3. Jumlah Data pada File")
            print("4. Save Data pada File")
            print("5. Buat Data Baru")
            print("6. Keluar")

            pilihan = input("Silakan Pilih Opsi: ")

            if pilihan == '1':
                self.user_data.detail_pribadi()
            elif pilihan == '2':
                self.user_data.ubah_nama()
            elif pilihan == '3':
                self.jumlah_data_pada_file()
            elif pilihan == '4':
                self.save_data_pada_file()
            elif pilihan == '5':
                self.user_data.buat_data_baru()
            elif pilihan == '6':
                self.keluar()
                break
            else:
                print("Pilihan tidak valid. Silakan pilih kembali.")


    def jumlah_data_pada_file(self):
        try:
            print("="*50)
            self.file = input("Masukkan nama file: ")
            self.file_name = f"{self.file}.txt"
            with open(self.file_name, 'r') as file:
                data = file.read()
                if data.strip() == '':
                    print("="*50)
                    print(f"Tidak Terdapat File dengan Nama {self.file_name}")
                else:
                    set_count = data.count("Nama")
                    print(f"Jumlah data pada file {self.file_name}: {set_count}")
        except FileNotFoundError:
            print(f"Tidak Terdapat File dengan Nama {self.file_name}")
            print(f"Jumlah data pada file : 0")


    def save_data_pada_file(self):
        try:
            if self.user_data.nama or self.user_data.email or self.user_data.password:
                print("="*50)
                self.file = input("Masukkan nama file: ")
                self.file_name = f"{self.file}.txt"
                with open(self.file_name, 'a+') as file:
                    file.seek(0)
                    data = file.read()
                    if data.strip() == '':
                        file.write("="*50 + "\n")
                    file.write(f"{'Nama':<20}: {self.user_data.nama}\n")
                    file.write(f"{'Email':<20}: {self.user_data.email}\n")
                    file.write(f"{'Password':<20}: {self.user_data.password}\n")
                    file.write("="*50 + "\n")
                self.user_data.nama = ""
                self.user_data.email = ""
                self.user_data.password = ""                
                print(f"Data berhasil disimpan di file {self.file_name}")
            else:
                print("="*50)
                print("Data saat ini kosong")
        except FileNotFoundError:
            print("="*50)
            print(f"Tidak Terdapat File dengan Nama {self.file_name}")


    def keluar(self):
        print("="*50)
        print("Sampai Jumpa Lagi")



if __name__ == "__main__":
    main_menu = MainMenu()
    main_menu.start()