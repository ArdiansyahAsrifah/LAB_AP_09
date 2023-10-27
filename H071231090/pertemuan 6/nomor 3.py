angka = input("Masukkan beberapa angka: ").split()
angka = [int(x) for x in angka]

angka_genap = []
angka_ganjil = []
angka_habis_dibagi_5 = []

for num in angka:
    if num % 2 == 0:
        angka_genap.append(num)
    else:
        angka_ganjil.append(num)
    if num % 5 == 0:
        angka_habis_dibagi_5.append(num)

print("Angka Genap:", angka_genap)
print("Angka Ganjil:", angka_ganjil)
print("Angka yang habis dibagi 5:", angka_habis_dibagi_5)