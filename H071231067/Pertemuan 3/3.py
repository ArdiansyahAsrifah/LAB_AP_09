while True:
    derajat=float(input('Masukkan Derajat= '))
    if derajat>=0 and derajat<=360:break
    else:print('Tidak Valid')

total_detik=derajat*240
jam=total_detik//3600+6
if jam>=24:
    jam=jam-24
sisa_detik=total_detik%3600
menit=sisa_detik//60 
detik=sisa_detik%60 
    
waktu = "{:02d}:{:02d}:{:02d}".format(int(jam), int(menit), int(detik))
if jam>=0 and jam<=10:print('Selamat Pagi')
elif jam>=11 and jam<=14:print('Selamat Siang')
elif jam>=15 and jam<=17:print('Selamat Sore')
elif jam>=18 and jam<=23:print('Selamat Malam')
print(waktu)