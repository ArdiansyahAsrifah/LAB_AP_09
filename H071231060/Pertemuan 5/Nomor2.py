kata = input("input kata : ")
kata = kata.replace(" ", "")
if len(kata) < 3:
    print("String input terlalu pendek.")
    exit()
def AwalTengahAkhir(karakter):
    panjang = len(karakter) 

    awal = karakter[0]
    huruf_tengah = panjang // 2
    if panjang % 2 == 0:
        tengah = karakter[huruf_tengah - 1:huruf_tengah + 1]
    else:
        tengah = karakter[huruf_tengah]
    akhir = karakter[-1]
    hasil = f"{awal}{tengah}{akhir}"

    return hasil

hasil_string = AwalTengahAkhir(kata)
print("String baru:", hasil_string)