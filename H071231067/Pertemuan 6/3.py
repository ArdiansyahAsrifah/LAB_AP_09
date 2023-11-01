angka=input('Masukkan beberapa angka: ')
list_angka = [int(angka) for angka in angka.split(' ')]

genap=[]
ganjil=[]
dibagi_5=[]
for x in list_angka:
    if x%2==0:
        genap.append(x)
    if x%2==1:
        ganjil.append(x)
    if x%5==0:
        dibagi_5.append(x)

print('Angka Genap:',genap)
print('Angka Ganjil:',ganjil)
print('Angka yang habis dibagi 5:',dibagi_5)