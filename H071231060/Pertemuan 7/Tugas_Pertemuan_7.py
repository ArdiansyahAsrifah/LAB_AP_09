from datetime import datetime
import os
import random


if not os.path.exists("invoices"):
    os.mkdir("invoices")


def cetak_invoice(kasir, items):
    now = datetime.now()
    id_transaksi = kasir[:3].upper() + now.strftime("%y%m%d%H%M") + str(random.randint(100, 999))
    NamaFile = f"invoices/{id_transaksi}.txt"

    with open(NamaFile, "w") as file:
        file.write("="*75 + "\n")
        file.write("|{:^73}|\n".format("DAFTAR TRANSAKSI"))
        file.write("="*75 + "\n")
        file.write("|{:^21}|{:^21}|{:^29}|\n".format("Waktu", "ID Transaksi", "Nominal Transaksi"))
        file.write("="*75 + "\n")
        catat_riwayat_transaksi(now, id_transaksi, total_harga)
        file.write("|{:^21}|{:^21}|{:^29}|\n".format(now.strftime('%d/%m/%y %H:%M'), id_transaksi, f"Rp.{total_harga:.2f}"))
        file.write("="*75 + "\n")

        file.write("|{:^15}|{:^20}|{:^15}|{:^20}|\n".format("Nama Produk", "Harga Produk", "Jumlah", "Subtotal"))
        file.write("="*75 + "\n")
        for item in items:
            nama_produk, harga, jumlah = item
            subtotal = harga * jumlah
            file.write("|{:^15}|{:^20}|{:^15}|{:^20}|\n".format(nama_produk, f"Rp.{harga:.2f}", jumlah, f"Rp.{subtotal:.2f}"))
        file.write("="*75 + "\n")

    return id_transaksi

# Fungsi untuk mencatat riwayat transaksi
def catat_riwayat_transaksi(waktu, id_transaksi, total_harga):
    with open("trx_history.txt", "a") as history_file:
        history_file.write(f"|{waktu.strftime('%d/%m/%y %H:%M')}|ID Transaksi nya :{id_transaksi:<20}|Total :{f'Rp.{total_harga:.2f}':>23}|\n")
        history_file.write("="*70 + "\n")

# Program utama
while True:
    print("Pilihan:")
    print("1. Melakukan Transaksi")
    print("2. Mencari Invoice Transaksi Sebelumnya")
    print("3. Keluar")
    
    pilihan = input("Pilih opsi (1/2/3): ")
    
    if pilihan == "1":
        kasir = input("Masukkan Nama Kasir: ")
        items = []
        total_harga = 0
        
        while True:
            nama_produk = input("Masukkan Nama Produk (ketik 'selesai' untuk menyelesaikan transaksi): ")
            if nama_produk.lower() == 'selesai':
                break
            else:
                harga = float(input("Masukkan Harga Produk: "))
                jumlah = int(input("Masukkan Jumlah Produk yang Dibeli: "))
                items.append((nama_produk, harga, jumlah))
                subtotal = harga * jumlah
                total_harga += subtotal
                
        if items:
            transaction_id = cetak_invoice(kasir, items)
            print(f"Invoice telah dicetak dengan ID transaksi: {transaction_id}")
            catat_riwayat_transaksi(datetime.now(), transaction_id, total_harga)
        else:
            print("Transaksi kosong. Tidak ada invoice yang dicetak.")

    elif pilihan == "2":
        id_transaksi = input("Masukkan ID Transaksi yang ingin Anda cari: ")
        nama_file = f"invoices/{id_transaksi}.txt"
    
        try:
            with open(nama_file, "r") as file:
                isi_invoice = file.read()
            print(f"Invoice untuk ID Transaksi {id_transaksi}:\n")
            print(isi_invoice)
        except FileNotFoundError:
            print(f"Invoice dengan ID Transaksi {id_transaksi} tidak ditemukan.")
    
    elif pilihan == "3":
        print("Terima kasih! Sampai jumpa.")
        break
    
    else:
        print("Pilihan tidak valid. Silakan pilih opsi yang benar (1/2/3).")