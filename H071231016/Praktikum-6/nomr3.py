angka = input("Masukkan beberapa angka: ").split()
angka = list(map(int,angka))
genap, ganjil, habis5, nol= [],[],[],[]
for i in angka:
    if i % 2 == 0 and i != 0:
        genap.append(i)
    if i % 2 != 0:
        ganjil.append(i)
    if i % 5 == 0 and i != 0:
        habis5.append(i)
    if i == 0:
        nol.append(i)
print(f"\nAngka nol : {nol}\nAngka Genap : {genap}\nAngka Ganjil: {ganjil}\nAngka yang habis dibagi 5 : {habis5}")