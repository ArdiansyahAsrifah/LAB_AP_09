def kategorikan_angka(angka):
    angka_genap = []
    angka_ganjil = []
    angka_dibagi_5 = []

    for a in angka:
        if a % 2 == 0:
            angka_genap.append(a)
        else:
            angka_ganjil.append(a)
        if a % 5 == 0:
            angka_dibagi_5.append(a)

    return angka_genap, angka_ganjil, angka_dibagi_5

# Input angka dari pengguna
input_angka = input("Masukkan beberapa angka (pisahkan dengan spasi): ")
angka_list = [int(x) for x in input_angka.split()]

# Kategorikan angka
angka_genap, angka_ganjil, angka_dibagi_5 = kategorikan_angka(angka_list)

# Tampilkan hasil
print("Angka Genap:", angka_genap)
print("Angka Ganjil:", angka_ganjil)
print("Angka yang habis dibagi 5:", angka_dibagi_5)