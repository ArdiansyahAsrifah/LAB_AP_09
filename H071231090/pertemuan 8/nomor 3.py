import re

username_pattern = r"^[A-Za-z\d]{5,20}$"
email_pattern = r"^[a-z]+(\d{2,})*@[a-z]+\.(com|co\.id)$"
password_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{8,}$"

while True:
    username = input("Masukkan username: ")
    if re.match(username_pattern, username):
        email = input("Masukkan email: ")
        if re.match(email_pattern, email):
            password = input("Masukkan password: ")
            if re.match(password_pattern, password):
                print(f"\nRegistrasi berhasil! Selamat datang {username}")
                break
            else:
                print("\nPassword yang kamu input beresiko dihack. Registrasi gagal.")   
        else:
            print("\nEmail yang kamu input tidak valid. Registrasi gagal!")
    else:
        print("\nInputan username tidak valid dalam sistem. Registrasi gagal!")