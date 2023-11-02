import re

karakter = input()
if len(karakter) == 45:
    cek = r"^[A-Za-z02468]{40}[13579\s]{5}$"

    if re.match(cek, karakter):
        print(True)
    else:
        print(False)
    
else:
    print("Panjang karakter harus 45")

