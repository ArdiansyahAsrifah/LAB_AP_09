import re

sentence = input("Masukkan String : ")
pattern = r"[A-Za-z2468]{40}[13579\s]{5}"
status = re.search(pattern, sentence)

if status:
    print(True)
else:
    print(False)
#2222222222aaaaaaaaaa2222222222aaaaaaaaaa13 57
#x4202v2A22A8a6aaaaaa2G2222m222qwertyYuIo1395779