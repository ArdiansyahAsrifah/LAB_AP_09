pengguna = {}

print('Selamat Datang untuk memulai silahkan input data anda')
pengguna["nama"] = input("Input nama: ")
pengguna["umur"] = input("Input umur: ")
pengguna["alamat"] = input("Input alamat: ")

while True:
    print("")
    print("="*100)
    print("Selamat Datang", pengguna["nama"],"silahkan pilih opsi")
    print("="*100)
    print("1.Detail Anda")
    print("2.Ubah Nama")
    print("3.Ubah Umur")
    print("4.Ubah Alamat")
    print("5.Keluar")
    print("="*100)
    
    opsi = input("Input opsi: ")

    if opsi == "1":
        print("="*100)
        print("Data anda adalah")
        print("Nama:",pengguna["nama"])
        print("Umur:", pengguna["umur"])
        print("Alamat:", pengguna["alamat"])
    elif opsi == "2":
        pengguna["nama"] = input("Silahkan Input nama baru:")
        print("Data anda sukses diperbarui")
    elif opsi == "3":
        pengguna["umur"] = input("Silahkan Input umur baru: ")
        print("Data anda sukses diperbarui")
    elif opsi == "4":
        pengguna["alamat"] = input("Silahkan Input alamat baru: ")
        print("Data anda sukses diperbarui")
    elif opsi == "5":
        print("=" * 100)
        print("Selamat Tinggal", pengguna["nama"])
        break
    else:
        print("Silahkan pilih opsi 1-5")

