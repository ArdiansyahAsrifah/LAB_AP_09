print('Selamat datang untuk memulai silahkan input data anda')
nama=input('Input nama: ')
while True:
    try:
        umur=int(input('Input umur: '))
        break
    except ValueError:
        print('Input harus angka,silahkan coba lagi')
alamat=input('Input alamat: ')

data={
    'nama':nama,
    'umur':umur,
    'alamat':alamat      
}      
      
while True:
    print('')
    print('='*60)
    print('Selamat datang',data['nama'],'silahkan pilih opsi')
    print('='*60)
    print('1. Detail anda')
    print('2. Ubah Nama')
    print('3. Ubah Umur')
    print('4. Ubah Alamat')
    print('5. Keluar')
    print('='*60)
    pilihan=input('Input opsi: ')
    print('='*60)

    if pilihan=='1':
        print('Data anda adalah')
        print('nama:',data['nama'])
        print('Umur:',data['umur'])
        print('Alamat:',data['alamat'])
    elif pilihan=='2':
        nama_baru=str(input('Silahkan Input nama baru: '))
        data['nama']=nama_baru
        print('Data anda sukses diperbarui')
    elif pilihan=='3':
       while True:
            try:
                umur_baru=int(input('Silahkan Input umur baru: '))
                data['umur']=umur_baru
                print('Data anda sukses diperbarui')
                break
            except ValueError:
                print('Input harus angka,silahkan coba lagi')
    elif pilihan=='4':
        alamat_baru=str(input('Silahkan Input alamat baru: '))
        data['alamat']=alamat_baru
        print('Data anda sukses diperbarui')
    elif pilihan=='5':
        print('Selamat Tinggal',data['nama'])
        break
    else:
        print('Silahkan pilih dari angka 1-5')
        