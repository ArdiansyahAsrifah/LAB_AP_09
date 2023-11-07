import re
def is_valid(string, pattern):
     return re.search(pattern, string)

username = input("Masukkan username: ")
if not is_valid(username, r"^[A-Za-z0-9]{5,20}$"): 
     print("\nInputan username tidak valid dalam sistem. Registrasi gagal!")
     exit()

email = input("Masukkan email: ")
if not is_valid(email, r"^[a-z0-9.*]+@[a-z]+\.(com|co\.id)$"):
    print("\nEmail yang kamu input tidak valid. Registrasi gagal!")
    exit()

password = input("Masukkan password: ")
if not is_valid(password, r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z0-9]{8,}$"):
    print("\nPassword yang kamu input beresiko dihack. Registrasi gagal.")
    exit()
print(f"\nRegistrasi berhasil! Halo, {username}")

ip_address = "121.203.197.20"
if re.match(r"^(25[0-5]|2[0-4][0-9]|[1-9]?[0-9]?)\.{3,3}(25[0-5]|2[0-4][0-9]|[1-9]?[0-9]?)$", ip_address):
    print("Alamat IP valid")
else:
     print("Alamat IP tidak valid")