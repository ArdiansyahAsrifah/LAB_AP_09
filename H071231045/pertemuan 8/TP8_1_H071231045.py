import re

kalimat = input("Masukkan String : ")
pattern = r"[A-Za-z2468]{40}[13579\s]{5}"
status = re.search(pattern, kalimat)

if status:
    print(True)
else:
    print(False)
    