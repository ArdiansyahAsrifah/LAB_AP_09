# Inisialisasi data
data = {
    'nama': '',
    'umur': '',
    'alamat': ''
}

# Main program
print("Selamat datang! Untuk memulai, silahkan input data anda.")
data['nama'] = input("Input nama: ")
data['umur'] = int(input("Input umur: "))
data['alamat'] = input("Input alamat: ")

# Perulangan untuk memilih opsi
while True:
    print("="*50)
    print(f"Selamat datang {data['nama']}! Silahkan pilih opsi")
    print("="*50)
    print("1. Detail anda")
    print("2. Ubah Nama")
    print("3. Ubah Umur")
    print("4. Ubah Alamat")
    print("5. Keluar")
    print("="*50)
    
    # Meminta input opsi dari pengguna
    opsi = input("Input opsi: ")

    # Menghandle opsi yang dipilih
    if opsi == '1':
        print("="*50)
        print("Data anda adalah")
        print("Nama:", data['nama'])
        print("Umur:", data['umur'])
        print("Alamat:", data['alamat'])
        print("="*50)
    elif opsi == '2':
        nama_baru = input("Silahkan Input nama baru: ")
        data['nama'] = nama_baru
        print("Data anda sukses di diperbarui")
    elif opsi == '3':
        umur_baru = int(input("Silahkan Input umur baru: "))
        data['umur'] = umur_baru
        print("Data anda sukses di diperbarui")
    elif opsi == '4':
        alamat_baru = input("Silahkan Input alamat baru: ")
        data['alamat'] = alamat_baru
        print("Data anda sukses di diperbarui")
    elif opsi == '5':
        print("="*50)
        print("Selamat Tinggal", data['nama'])
        break  # Keluar dari perulangan jika memilih opsi 5
    else:
        print("Opsi tidak valid. Silakan coba lagi.")  # Pesan untuk opsi tidak valid
