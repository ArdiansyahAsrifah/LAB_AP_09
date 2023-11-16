import os.path
import re
hasil_nama = ''
hasil_email = ''
hasil_password = '' 
def garis(angka):
    return '='*angka
def cek_email(email):
    pattern = r'^[a-z\d]+@student\.unhas\.ac\.id$'
    return re.match(pattern, email)

while True:
    print(garis(50))
    print('Selamat Datang Silahkan Pilih Opsi Menu Anda')
    print(' 1. Detail Anda')
    print(' 2. Ubah Nama')
    print(' 3. Jumlah Data pada File')
    print(' 4. Save Data pada File')
    print(' 5. Buat Data Baru')
    print(' 6. Keluar')
    opsi = input('Silahkan Pilih Opsi Anda : ')
    print(garis(50))
    
    if opsi == '1':
        if len(hasil_email) > 0:
            print('Data anda adalah')
            print(f'Nama : {hasil_nama}')
            print(f'Email : {hasil_email}')
            print(f'Password : {hasil_password}')
        else:
            print('Data saat ini Kosong')
        
    elif opsi == '2':
        if len(hasil_nama) > 0:
            nama_baru = input('Silahkan Input Nama Baru : ')
            hasil_nama = nama_baru
        else:
            print('Data saat ini Kosong')
            
    elif opsi == '3':
        file_path_cari = input('Silahkan Masukkan Nama File : ')
        if os.path.exists('Pertemuan 10' +'/'+ file_path_cari + '.txt'):
            with open('Pertemuan 10' +'/'+ file_path_cari + '.txt', 'r') as files:
                teks = files.read()
                jumlah = teks.count('+================================================================================')
                jumlah2 = -2 + jumlah
            print('Berhasil')
            print(f'Jumlah Data Pada File : {jumlah2}')
            pass
        else:
            print(f'Tidak Terdapat File dengan nama {file_path_cari}.txt')
            print('Jumlah Data Pada File : 0 Data')
            
    elif opsi == '4':
        teks_file = f'''                             
        +================================================================================
        |Data yang Tersimpan
        +================================================================================
        |Nama      :{hasil_nama}
        |Email     :{hasil_email}                                                  
        |Password  :{hasil_password}
        +================================================================================'''

        tambah_teks_file = f'''
        |Nama      :{hasil_nama}
        |Email     :{hasil_email}
        |Password  :{hasil_password}
        +================================================================================'''  
        if len(hasil_email) > 0:
            nama_file = input('Silahkan Masukkan nama File : ')
            file_path = 'Pertemuan 10'+ '/' + nama_file +'.txt'
            if not os.path.exists(file_path):
                with open(file_path, 'w') as file:
                    file.write(teks_file)
                hasil_nama = ''
                hasil_email = ''
                hasil_password = ''
                print('Berhasil')
            else:
                with open(file_path, 'a') as file2:
                    file2.write(tambah_teks_file)
                hasil_nama = ''
                hasil_email = ''
                hasil_password = ''
                print('Berhasil')
        else:
            print('Data saat ini Kosong')
    
    elif opsi == '5':
        nama = input('Silahkan Masukkan Nama Anda : ')
        if hasil_nama == '':
            hasil_nama += nama
        else:
            hasil_nama = nama
        while True:
            email = input('Silahkan Masukkan Email Anda : ')
            if cek_email(email):
                if hasil_email == '':
                    hasil_email += email
                else:
                    hasil_email = email
                break
            else:
                print(garis(50))
                print('Email yang Anda Masukkan Salah')
                print(garis(50))
        while True:
            password = input('Silahkan Masukkan Password Anda : ')
            pattern = (r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,20}$')

            if len(password) < 8 or len(password) > 20:
                print(garis(50))
                print('Password harus memiliki Panjang 8 - 20 karakter')
                print(garis(50))
            elif not re.match(pattern,password):
                print(garis(50))
                print('Password yang anda masukkan terlalu lemah')
                print('Gunakan Minimal 1 Huruf Kapital, Huruf Kecil, dan Angka')
                print(garis(50))
            else:
                if hasil_password == '':
                    hasil_password += password
                else:
                    hasil_password = password
                break
            
    elif opsi == '6':
        print('Sampai Jumpa Lagi')
        break
    
    else:
        print('Silahkan pilih 1-5')