kata=input('Masukkan Kata : ').replace(' ','')

panjang_kata=len(kata)
kata2=kata[0]+kata[(panjang_kata//2)]+kata[-1]

if panjang_kata<3:
    print('Error')
else:
    print(kata2)