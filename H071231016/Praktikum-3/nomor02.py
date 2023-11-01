hargaBarang =  int(input("Masukkan Harga Barang: "))
uang = int(input("Masukkan Uang Anda: "))

kembalian = uang - hargaBarang

pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

if hargaBarang > uang:
    print("uang anda tidak cukup, dilarang utang disini!")
    exit()
for pecahan in pecahan_uang:
    jumlah_uang = kembalian // pecahan
    kembalian %= pecahan
    print(f"{jumlah_uang} uang sejumlah Rp.{pecahan} ")

#nah jumlah_uang itu adalah lembar uang yang dikembalikan nantinya
