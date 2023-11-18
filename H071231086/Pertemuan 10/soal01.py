import re
import os

class UserData:
    def __init__(self):
        self.nama = ""
        self.email = ""
        self.password = ""

    def set_data(self, nama, email, password):
        self.nama = nama
        self.email = email
        self.password = password

    def show_data(self):
        if not self.nama:
            print("Data saat ini kosong.")
        else:
            print("\nDetail Data Anda:")
            print(f"Nama: {self.nama}")
            print(f"Email: {self.email}")
            print(f"Password: {self.password}")

    def change_name(self, new_name):
        if not self.nama:
            print("Data saat ini kosong.")
        else:
            self.nama = new_name
            print("Nama telah diubah.")

    def is_email_valid(self, email):
        pattern = r"^[a-z0-9]+@student\.unhas\.ac\.id$"
        return bool(re.match(pattern, email))

    def is_password_valid(self, password):
        return (
            8 <= len(password) <= 20
            and any(char.isupper() for char in password)
            and any(char.islower() for char in password)
            and any(char.isdigit() for char in password)
        )

    def create_new_data(self):
        nama = input("Masukkan Nama: ")
        email = input("Masukkan Email: ")

        while not self.is_email_valid(email):
            print("Email yang Anda Masukkan Salah")
            email = input("Masukkan Email: ")

        password = input("Masukkan Password: ")
        while not self.is_password_valid(password):
            print("Password harus memiliki Panjang 8 – 20 karakter "
                  "dan minimal 1 huruf kapital, huruf kecil, dan angka")
            password = input("Masukkan Password: ")

        self.set_data(nama, email, password)
        print("Data baru telah dibuat.")

    def save_data_to_file(self, file_name):
        with open(f"{file_name}.txt", "a") as file:
            if os.path.getsize(f"{file_name}.txt") == 0:
                file.write("+===============================================================================\n")
                file.write("| Data yang tersimpan\n")
                file.write("+===============================================================================\n")
            
            file.write(f"| Nama     : {self.nama}\n")
            file.write(f"| Email    : {self.email}\n")
            file.write(f"| Password : {self.password}\n")
            file.write("+===============================================================================\n")
        print("Data berhasil disimpan.")
        self.clear_data()

    def clear_data(self):
        self.nama = ""
        self.email = ""
        self.password = ""


def menu_detail(data):
    data.show_data()


def menu_ubah_nama(data):
    if not data.nama :
        print("Data saat ini kosong")
    else :
        data.change_name(input("Masukkan Nama Baru: "))


def menu_jumlah_data(file_name):
    try:
        with open(f"{file_name}.txt", "r") as file:
            lines = file.readlines()
            saved_data_counter = sum(1 for line in lines if line.startswith("| Nama"))
            print(f"Jumlah data pada file {file_name}.txt: {saved_data_counter}")
    except FileNotFoundError:
        print(f"Tidak Terdapat File dengan Nama {file_name}.txt")
        print(f"Jumlah data Pada File : 0 Data")


def menu_save_data(data, file_name):
    if not data.nama:
        print("Data saat ini kosong.")
    else:
        file_name = file_name
        data.save_data_to_file(file_name)


def menu_buat_data(data):
    data.create_new_data()


def main():
    user_data = UserData()

    while True:
        print("===============================================")
        print("Selamat Datang Silahkan Pilih Opsi Menu Anda")
        print(" 1. Detail Anda")
        print(" 2. Ubah Nama")
        print(" 3. Jumlah Data pada File")
        print(" 4. Save Data pada File")
        print(" 5. Buat Data Baru")
        print(" 6. Keluar")

        choice = input(" Silahkan Pilih Opsi Anda : ")

        if choice == '1':
            print("===============================================")
            menu_detail(user_data)
        elif choice == '2':
            print("===============================================")
            menu_ubah_nama(user_data)
        elif choice == '3':
            print("===============================================")
            file_name = input(" Silahkan Masukkan Nama File :  ")
            menu_jumlah_data(file_name)
        elif choice == '4':
            print("===============================================")
            if not user_data.nama:
                print("Data saat ini kosong.")
            else:
                file_name = input(" Silahkan Masukkan Nama File : ")
                menu_save_data(user_data, file_name)
        elif choice == '5':
            print("===============================================")
            menu_buat_data(user_data)
        elif choice == '6':
            print("===============================================")
            print(" Sampai Jumpa Lagi!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")

if __name__ == "__main__":
    main()
