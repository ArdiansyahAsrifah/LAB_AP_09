import os.path
import datetime
import random

# fungsi untuk membuat garis tabel lurus satu sama lain
def garis_tabel(kata,len_kata_atas,arah):
    if len(kata)>len_kata_atas:
        kata=kata[:(len_kata_atas-3)]+'...'
        
    elif len(kata)<len_kata_atas and arah=='kiri':
        kata=kata+(' '*(len_kata_atas-len(kata)))
        
    elif len(kata)<len_kata_atas and arah=='kanan':
        kata=(' '*(len_kata_atas-len(kata)-1))+kata+' '
            
    elif len(kata)<len_kata_atas and arah=='tengah':
        if len_kata_atas%2 == 1 and len(kata)%2 == 1 and len(kata)!=1:
            kata=' '*2 + (' '*(len_kata_atas//2-len(kata)//2))+ kata +(' '*(len_kata_atas//2-len(kata)//2))
        elif len_kata_atas%2 == 0 and len(kata)%2 == 0:
            kata=(' '*(len_kata_atas//2-len(kata)//2))+ kata +(' '*(len_kata_atas//2-len(kata)//2))
        elif len_kata_atas%2 == 0 and len(kata) == 1:
            kata=(' '*(len_kata_atas//2-len(kata)//2))+ kata +(' '*(len_kata_atas//2-len(kata)//2-1))
        else:
            kata=(' '*(len_kata_atas//2-len(kata)//2-1))+ kata +(' '*(len_kata_atas//2-len(kata)//2))
            
    return kata

# untuk waktu di transaksi invoice dan history
waktu = datetime.datetime.now()
format_tanggal=waktu.strftime('%d/%m/%y'+' ''%H:%M')
format_tanggal=str(format_tanggal)

# untuk waktu di nama file invoice
dua_digit_tahun = str(waktu.strftime('%y'))
digit_bulan = str(waktu.strftime('%m'))
digit_hari = str(waktu.strftime('%d'))
empat_digit_jam = str(waktu.strftime('%H%M'))

# untuk history
list_invoice=[]
list_total_harga=[]
list_format_tanggal=[]

print('='*60)
print('SELAMAT DATANG'.center(60))
print('='*60)
nama_kasir=input('Masukkan nama kasir          : ')

# inisial mengambil huruf pertama,tengah,dan akhir
panjang_kata=len(nama_kasir)
if panjang_kata>=3:
    inisial_nama=(nama_kasir[0]+nama_kasir[(panjang_kata//2)]+nama_kasir[-1]).upper()
else:
    inisial_nama=nama_kasir.upper()

while True:
    print('='*60)
    print('Pilih opsi :')
    print('1. Transaksi Baru')
    print('2. Cari Transaksi')
    print('3. Keluar')
    print('='*60)
    while True:
        try:
            opsi_pilihan=int(input('Masukkan opsi pilihan        : '))
            if opsi_pilihan in(1,2,3):
                break
            else:
                print('Masukkan angka 1-3,silahkan coba lagi')
        except ValueError:
            print('Masukkan angka 1-3,silahkan coba lagi')
    print('='*60)

    daftar= {
            'nama':[],
            'harga':[],
            'jumlah':[]
    }
    if opsi_pilihan==1:
        nilai_acak = str(random.randint(100,999))
        while True:
            nama_produk  =input('Masukkan nama produk         : ')
            daftar['nama'].append(nama_produk)
            while True:
                try:
                    harga_produk =int(input('Masukkan harga produk        : '))
                    daftar['harga'].append(harga_produk)
                    break
                except ValueError:
                    print('Silahkan masukkan angka')
            while True:
                try:
                    jumlah_produk=int(input('Masukkan jumlah produk       : '))
                    daftar['jumlah'].append(jumlah_produk)
                    break
                except ValueError:
                    print('Silahkan masukkan angka')
            
            print('='*60)
            while True:
                try:
                    tambah=input('Tambah produk? (y/t)         : ').lower()
                    if tambah in('y','t'):
                        break
                    else:
                        print('Silahkan pilih y atau t')
                except ValueError:
                    print('Silahkan pilih y atau t')
            print('='*60)
            if tambah=='t':    
                break
        print('TRANSAKSI BERHASIL'.center(60))
        
        # untuk list harga tiap produk di 1 transaksi dan total harga per 1 transaksi 
        list_harga=[]
        for i in range(len(daftar['harga'])):
            x=daftar['harga'][i] * daftar['jumlah'][i]
            list_harga.append(x)
        total_harga=sum(list_harga)
        list_total_harga.append(total_harga)

        # template teks untuk invoice
        teks_invoice = f'''
                                    TOKO {nama_kasir.upper()}                                 

        ================================================================================
        Nama Kasir          : {nama_kasir}
        Waktu Transaksi     : {format_tanggal}
        ================================================================================

                                        Daftar Produk                                  

            ========================================================================   
            |        Nama       |     Harga      |     Jumlah     |     Total      |
            ========================================================================''' 
        for i in range(len(daftar['nama'])):
            teks_invoice +=f'''
            | {garis_tabel(daftar['nama'][i],18,'kiri')}|{garis_tabel('Rp'+str(daftar['harga'][i]),15,'kanan')} |{garis_tabel(str(daftar['jumlah'][i]),16,'tengah')}|{garis_tabel('Rp'+str(list_harga[i]),15,'kanan')} |
            ========================================================================'''
        teks_invoice +=f'''
            |     TOTAL                                           |{garis_tabel('Rp'+str(total_harga),15,'kanan')} |
            ========================================================================    

        ================================================================================
                                TERIMA KASIH TELAH BERBELANJA                          
        ================================================================================'''
        
        # untuk write teks invoice
        invoices = inisial_nama + dua_digit_tahun + digit_bulan + digit_hari + empat_digit_jam + nilai_acak
        list_format_tanggal.append(format_tanggal)
        list_invoice.append(invoices)
        folder_path = 'Pertemuan 7'+'/'+'invoices'
        file_path = folder_path + '/' + invoices + '.txt'
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        with open(file_path, 'w') as invoice:
            invoice.write(teks_invoice)
        
        
        # template untuk teks history
        teks_history= f'''
        ====================================================================================
        |                                   RIWAYAT TRANSAKSI                              |
        ====================================================================================
        |        Waktu         |       ID Transaksi         |       Nominal Transaksi      |
        ===================================================================================='''
        for i in range(len(list_invoice)):
            teks_history2=f'''
        |{garis_tabel(str(list_format_tanggal[i]),22,'tengah')}| {garis_tabel(list_invoice[i],27,'kiri')}|{garis_tabel('Rp'+str(list_total_harga[i]),30,'kanan')}|
        ===================================================================================='''
            
        # untuk write teks history
        folder_path='Pertemuan 7'
        file_path=folder_path+'/'+'trx_history'+'.txt'
        if not os.path.exists(file_path):
            with open(file_path,'w') as history:
                history.write(teks_history)
            with open(file_path,'a') as history2:
                history2.write(teks_history2)
        else:
            with open(file_path,'a') as history2:
                history2.write(teks_history2)
    
    
    elif opsi_pilihan==2:
        id_transaksi=input('Masukkan ID transaksi        : ')
        folder_path = 'Pertemuan 7'+'/'+'invoices'
        file_path = folder_path + '/' + id_transaksi + '.txt'
        try:
            if os.path.exists(file_path):
                with open(file_path,'r') as transaksi:
                    isi_transaksi=transaksi.read()
                print(isi_transaksi)
            else:
                print('ID Transaksi Tidak Ditemukan')
        except FileNotFoundError or NameError:
            print('ID Transaksi Tidak Ditemukan')
                      
    elif opsi_pilihan==3:
        print('SAMPAI JUMPA'.center(60))
        print('='*60)
        break