array_1=input('Input array ke-1: ')
array_2=input('Input array ke-2: ')
list_angka1 = {int(array_1) for array_1 in array_1.split(' ')}
list_angka2 = {int(array_2) for array_2 in array_2.split(' ')}
hasil=list_angka1&list_angka2
list=str(hasil).replace('{', '(').replace('}', ')')

if len(hasil)>0:
    print('Terdapat',len(hasil),'buah duplikat yaitu',list)
else:
    print('Tidak ada duplikasi ditemukan.')