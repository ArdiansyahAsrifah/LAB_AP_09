import os
import random
import datetime

if not os.path.exists("invoices"):
    os.mkdir("invoices")

# Buat atau buka file trx_history.txt untuk mencatat riwayat transaksi
with open("trx_history.txt", "a") as history_file:
    if os.path.getsize("trx_history.txt") == 0:  # Cek apakah file kosong
        history_file.write("=================================================================\n")
        history_file.write("|                      RIWAYAT TRANSAKSI                        |\n")
        history_file.write("=================================================================\n")
        history_file.write("|    Waktu       |    ID Transaksi     |    Nominal Transaksi   |\n")
        history_file.write("=================================================================\n")

print("============================================================")
print("                      SELAMAT DATANG                       ")
print("============================================================")
kasir = input("Masukkan Nama Kasir      : ")

while True:
    print("============================================================")
    print("Pilih Opsi :\n1. Transaksi Baru\n2. Cari Transaksi\n3. Keluar")
    print("============================================================")
    opsi = input("Masukkan Opsi Pilihan    : ")

    if opsi == "1":
        transaksi = []
        total = 0

        while True:
            print("=" * 60)
            nama_produk = input("Masukkan Nama Produk     : ")
            harga_produk = int(input("Masukkan Harga Produk    : "))
            jumlah_produk = int(input("Masukkan Jumlah Produk   : "))
            subtotal = harga_produk * jumlah_produk
            total += subtotal
            transaksi.append((nama_produk, harga_produk, jumlah_produk, subtotal))

            while True:
                print("=" * 60)
                tambah = input("Tambah Produk? (y/t)     : ").lower()
                if tambah == "y":
                    break
                elif tambah == "t":
                    print("============================================================")
                    print("                     TRANSAKSI BERHASIL                     ")

                    waktu_sekarang = datetime.datetime.now()
                    tanggal_transaksi = waktu_sekarang.strftime("%y%m%d%H%M")
                    angka_acak = str(random.randint(100, 999))
                    waktu_transaksi = waktu_sekarang.strftime("%d/%m/%y %H:%M")
                    id = f"{kasir[0]}{tanggal_transaksi}{angka_acak}"
                    file_invoice = f"{kasir[0]}{tanggal_transaksi}{angka_acak}.txt"

                    with open(f"invoices/{file_invoice}", "w") as file:
                        file.write("\n                              TOKO NAILAH\n\n")
                        file.write("======================================================================\n")
                        file.write(f"Nama Kasir          : {kasir}\n")
                        file.write(f"Waktu Transaksi     : {waktu_transaksi}\n")
                        file.write("======================================================================\n\n")
                        file.write("                             Daftar Produk\n\n")
                        file.write("     ============================================================\n")
                        file.write("     |        Nama        |   Harga    | Jumlah |     Total     |\n")
                        file.write("     ============================================================\n")
                        for produk in transaksi:
                            nama, harga, jumlah, subtotal = produk
                            if len(nama) > 19:
                                nama = nama[:16] + "..."
                            file.write(f"     | {nama.ljust(19)}| Rp{harga:<9}| {jumlah:<7}|  Rp{subtotal:<11}|\n")
                        file.write("     ============================================================\n")
                        file.write(f"     |        TOTAL                             |  Rp{total:<11}|\n")
                        file.write("     ============================================================\n\n")
                        file.write("======================================================================\n")
                        file.write("                      TERIMA KASIH TELAH BERBELANJA\n")
                        file.write("======================================================================\n")

                        # Menambah riwayat transaksi ke file trx_history.txt
                        with open("trx_history.txt", "a") as history_file:
                            history_file.write(f"| {waktu_transaksi} | {id:<20}| Rp{total:<21}|\n")
                            history_file.write("=================================================================\n")

                    break
                else:
                    print("Pilihan tidak valid. Harap masukkan 'y' atau 't'.")

            if tambah == "t":
                break

    elif opsi == "2":
        print("=" * 60)
        id_transaksi = input("Masukkan ID Transaksi   : ")
     
        try:
            with open(f"invoices/{id_transaksi}.txt", "r") as file:
                isi_invoice = file.read()
                print(isi_invoice)
        except FileNotFoundError:
            print("Invoice tidak ditemukan.")


    elif opsi == "3":
        print("============================================================")
        print("                        SAMPAI JUMPA                        ")
        print("============================================================")
        break
