data_pengguna = {
    'nama': '',
    'umur': '',
    'alamat': ''
}

def tampilkan_menu():
    print("Selamat datang untuk memulai, silahkan input data Anda")
    data_pengguna['nama'] = input("Input nama: ")
    data_pengguna['umur'] = int(input("Input umur: "))
    data_pengguna['alamat'] = input("Input alamat: ")
    print("=" * 50)
    print(f"Selamat datang {data_pengguna['nama']}, silahkan pilih opsi")
    while True:
        print("=" * 50)
        print("1. Detail Anda")
        print("2. Ubah Nama")
        print("3. Ubah Umur")
        print("4. Ubah Alamat")
        print("5. Keluar")
        pilihan = int(input("Input opsi: "))
        if pilihan == 1:
            detail_pengguna()
        elif pilihan == 2:
            ubah_nama()
        elif pilihan == 3:
            ubah_umur()
        elif pilihan == 4:
            ubah_alamat()
        elif pilihan == 5:
            print("Terima kasih, program telah selesai.")
            break
        else:
            print("Opsi tidak valid, silakan coba lagi.")

def detail_pengguna():
    print("=" * 50)
    print("Data Anda adalah")
    print(f"Nama: {data_pengguna['nama']}")
    print(f"Umur: {data_pengguna['umur']}")
    print(f"Alamat: {data_pengguna['alamat']}")

def ubah_nama():
    data_pengguna['nama'] = input("Masukkan nama baru: ")

def ubah_umur():
    data_pengguna['umur'] = int(input("Masukkan umur baru: "))

def ubah_alamat():
    data_pengguna['alamat'] = input("Masukkan alamat baru: ")

tampilkan_menu()