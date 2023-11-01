def string(a):
    panjang = len(a)
    karakter_pertama = a[0]
    karakter_terakhir = a[-1]
    karakter_tengah = a[panjang//2]
    string_baru = karakter_pertama + karakter_tengah + karakter_terakhir
    return string_baru

a = input("Masukkan String = ")
string_baru = string(a)
print(string_baru)