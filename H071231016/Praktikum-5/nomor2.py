kata = input("Masukkan kata: ")
hasil = len(kata)

if hasil % 2 == 0:
    hasil = kata [0] + kata [hasil//2 -1] + kata[hasil//2] + kata[-1]
else:
    hasil = kata [0] + kata[hasil//2] + kata[-1]

print (hasil)