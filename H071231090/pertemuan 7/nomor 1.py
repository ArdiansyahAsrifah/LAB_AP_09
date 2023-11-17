import os
import time
import random

if not os.path.exists("invoices"):
    os.mkdir("invoices")

def Id_Transaksi():
    waktu = time.strftime("%y%m%d%H%M", time.localtime())
    id_transaksi = f"{inisial}{waktu}{random.randint(100, 999)}"
    return id_transaksi

def cetak_invoice(id_transaksi, nama_kasir, produk, total_transaksi):
    invoice_filename = f"invoices/{id_transaksi}"
    with open(invoice_filename, "w") as file_invoice:
        file_invoice.write(f"TOKO {nama_kasir}".center(66).upper() + "\n")
        file_invoice.write("=" * 66 + "\n")
        file_invoice.write(f"{'Kasir':<20}:{nama_kasir}\n".title())
        file_invoice.write(f"{'Waktu transaksi':<20}:" + (time.strftime("%d/%m/%Y %H:%M", time.localtime()) + "\n"))
        file_invoice.write("=" * 66 + "\n")
        file_invoice.write("\n" + "Daftar Produk".center(66) + "\n")
        file_invoice.write(f"""
    {'=' * 58}
    |{'Nama':^20}|{'Harga':^12}|{'Jumlah':^8}|{'Total':^13}|
    {'=' * 58}""")
        for i in produk:
            nama, harga, jumlah = i
            if len(nama) > 15:
                nama = nama[:15] + "..."
            file_invoice.write(f"\n    | {nama:<18} |" + f"Rp.{harga:>8} |" + f" {jumlah:^6} " + f"|Rp.{harga * jumlah :>9} |")
        file_invoice.write('\n' + f"{'=' * 58}".center(66))
        file_invoice.write('\n' + f"    |{'TOTAL':^42}|Rp.{total_transaksi:>9} |" + "\n")
        file_invoice.write(f"{'=' * 58}".center(66) + f"\n\n{'=' * 66}\n" + 'TERIMA KASIH TELAH BERBELANJA'.center(66) + f"\n{'=' * 66}")


def mencari(id_transaksi):
    nama_file = f"invoices/{id_transaksi}.txt"
    if os.path.exists(nama_file):
        print(f"{'_' * 66}")
        with open(nama_file, 'r') as file_invoice:
            print(file_invoice.read())
        print(f"{'_' * 66}")
    else:
        print("Invoice tidak ditemukan")

def riwayat_transaksi(id_transaksi, total):
    riwayat_file = "trx_history.txt"
    waktu_transaksi = time.strftime("%d/%m/%Y %H:%M", time.localtime())
    if os.path.exists(riwayat_file) == False:
            with open(riwayat_file, 'w') as riwayat:
                riwayat.write(f"""
{'=' * 80}
|{'RIWAYAT TRANSAKSI':^78}|
{'=' * 80}
| {'Waktu':^20} | {'ID':^20} | {'Nominal':^30} |
{'=' * 80}
""") 
                riwayat.write(f"""
| {waktu_transaksi:^20} | {id_transaksi:^20} | Rp.{total:>27} |
{'=' * 80}""")
    else: 
            with open(riwayat_file, 'a') as riwayat:
                riwayat.write(f"""
| {waktu_transaksi:^20} | {id_transaksi:^20} | Rp.{total:>27} |
{'=' * 80}""")


print("=" * 50)
print("Selamat datang".center(50))
print("=" * 50)
nama_kasir = input("Masukkan nama kasir : ")
print(f"{'=' * 50}")
jumlah = len(nama_kasir)
inisial = (nama_kasir[0] + nama_kasir[jumlah//2] + nama_kasir[-1]).upper()

while True:
    print("Pilih opsi\n1. Transaksi baru\n2. Cari transaksi\n3. Keluar")
    print("=" * 50)
    option = input("Masukkan opsi pilihan : ")

    if option == "1":
        id_transaksi = f"{Id_Transaksi()}.txt"
        produk = []
        total = 0
        while True:
            print(f"{'=' * 50}")
            nama_produk = input("Masukkan nama produk : ")
            harga_produk = input("Masukkan harga produk : ")
            if harga_produk.isdigit():
                harga_produk = int(harga_produk)
                if harga_produk < 500:
                    print("Tidak sesuai harga")
                    continue
            else:
                print("Harga produk harus dalam bentuk angka.")
                continue

            jumlah_produk = int(input("Masukkan jumlah produk : "))

            produk.append((nama_produk, harga_produk, jumlah_produk))

            total += harga_produk * jumlah_produk

            tambah_produk = input(f"{'=' * 50}\n" + "Tambahkan produk (y/t) : ").lower()
            if tambah_produk != "y":
                break

        cetak_invoice(id_transaksi, nama_kasir, produk, total)
        riwayat_transaksi(id_transaksi.replace(".txt",""), total)
        print(f"{'=' * 50 }\n" + 'TRANSAKSI BERHASIL'.center(50) + f"\n{'=' * 50 }")

    elif option == "2":
        print(f"{'=' * 50}")
        id_transaksi = input("Masukkan ID transaksi: ")
        mencari(id_transaksi)

    elif option == "3":
        print(f"{'=' * 50}\n" + 'SAMPAI JUMPA'.center(50) + f"\n{'=' * 50}")
        break
    else:
        print("Opsi tidak valid")