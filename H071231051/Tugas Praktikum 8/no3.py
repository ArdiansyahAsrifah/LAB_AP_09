import re

cek_username = r"^[A-Za-z0-9]{5,20}$"
cek_email = r"^[a-z]+(\d{2,})*@[a-z]+\.(com|co\.id)$"
cek_password = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{8,}$"

while True:
    username = input("Masukkan username: ")
    if re.match(cek_username, username):
        email = input("Masukkan email: ")
        if re.match(cek_email, email):
            password = input("Masukkan password: ")
            if re.match(cek_password, password):
                print(f"\nRegistrasi berhasil! Selamat datang {username}")
                break
            else:
                print("\nPassword yang kamu input beresiko dihack. Registrasi gagal.")   
        else:
            print("\nEmail yang kamu input tidak valid. Registrasi gagal!")
    else:
        print("\nInputan username tidak valid dalam sistem. Registrasi gagal!")