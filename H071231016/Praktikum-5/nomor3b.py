kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

kata1 = kata1.lower().replace(" ","")
kata2 = kata2.lower().replace(" ","")

frekuensi1 = {}
frekuensi2 = {}

for i in kata1:
    if i in frekuensi1:
        frekuensi1[i] += 1
    else:
        frekuensi1[i] = 1

for i in kata2:
    if i in frekuensi2:
        frekuensi2[i] += 1
    else:
        frekuensi2[i] = 1

anagram = frekuensi1 == frekuensi2
print(anagram)
    