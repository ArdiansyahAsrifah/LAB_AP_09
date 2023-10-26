data = map(int,input('Masukkan beberapa angka : ').split(' '))
genap, ganjil, bagi5 = [], [], []

for i in data:
    if i % 2 == 0:
        genap.append(i)
    elif i % 2 != 0:
        ganjil.append(i)
    elif i % 5 == 0:
        bagi5.append(i)

print(f"Angka Genap : {genap}")
print(f"Angka Ganjil : {ganjil}")
print(f"Angka habis dibagi 5: {bagi5}")