def kategori(angka):
    angka_genap = []
    angka_ganjil = []
    angka_habis5 = []
    
    for i in angka:
        i = int(i)
        if i % 2 == 0:
            angka_genap.append(i)
        elif i % 2 == 1:
            angka_ganjil.append(i)
        if i % 5 == 0:
            angka_habis5.append(i)
    return f"Angka Genap : {angka_genap}\nAngka Ganjil : {angka_ganjil}\nAngka yang habis dibagi 5: {angka_habis5}"

angka = input("Masukkan beberapa angka: ").split()
print(kategori(angka))