print("Selamat datang! Untuk memulai, silakan input data anda")

def input_data():
    nama = input("Input nama: ")
    umur = int(input("Input umur: "))  # Menggunakan int() untuk mengambil umur sebagai integer
    alamat = input("Input alamat: ")
    return {
        "Nama": nama,
        "Umur": umur,
        "Alamat": alamat
    }

def halaman_utama():
    data_pengguna = input_data()
    while True:
        print("=" * 55 + f"\nSelamat datang, {data_pengguna['Nama']}! Silakan pilih opsi:\n" + "=" * 55 + "\n1. Detail anda\n2. Ubah Nama\n3. Ubah Umur\n4. Ubah Alamat\n5. Keluar\n" + "=" * 55)
        pilihan = input("Input opsi: ")
        
        match pilihan:
            case '1':
                print("=" * 55)
                print("Data Anda adalah:")
                for key, nilai in data_pengguna.items():
                    print(f"{key}: {nilai}")
            case '2':
                item = "Nama"
                data_pengguna[item] = input(f"Silakan Input {item} baru: ")
                print("Data anda sukses diperbarui")
            case '3':
                item = "Umur"
                data_pengguna[item] = int(input(f"Silakan Input {item} baru: "))  # Menggunakan int() untuk mengambil umur sebagai integer
                print("Data anda sukses diperbarui")
            case '4':
                item = "Alamat"
                data_pengguna[item] = input(f"Silakan Input {item} baru: ")
                print("Data anda sukses diperbarui")
            case '5':
                print("=" * 55 + f"\nSelamat Tinggal, {data_pengguna['Nama']}\n" + "=" * 55 + "\nTerima kasih! Program berakhir.")
                break
            case _:
                print("Pilihan tidak valid.")
                break
halaman_utama()


