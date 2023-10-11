s1 = input("Masukkan input pertama: ")
s2 = input("Masukkan input kedua: ")

result = ""

panjang_maks = max(len(s1), len(s2))

for i in range(panjang_maks):
    if i < len(s1):
        result += s1[i]
    if i < len(s2):
        result += s2[::-1][i]

print("Hasil campuran:",result)