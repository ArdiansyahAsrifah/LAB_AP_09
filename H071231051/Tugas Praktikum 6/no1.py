data = {}
    
print("Selamat datang untuk memulai silahkan input data anda")
data["Nama"] = input("Input nama: ")
umur = input("Input umur: ")
if umur.isdigit():
    data["Umur"] = umur
else:
    print("Umur harus berupa bilangan bulat")   
data["Alamat"] = input("Input alamat: ")

def mengubah_nama():
    data["Nama"] = input("Silahkan input nama baru : ")
    print("Data anda sukses di perbaharui")

def mengubah_umur():
    data["Umur"] = input("Silahkan input umur baru : ")
    print("Data anda sukses di perbaharui")

def mengubah_alamat():
    data["Alamat"] = input("Silahkan input alam baruat : ")
    print("Data anda sukses di perbaharui")

def detail_pengguna():
    print("Data anda adalah")
    print(f"Nama:", data.get("Nama"))
    print("Umur:", data.get("Umur"))
    print("Alamat:", data.get("Alamat"))

while True:
    print("=" * 40)
    print(f"Selamat datang {data['Nama']} silahkan pilih opsi")
    print("=" * 40)
    print(" 1. Detail anda\n 2. Ubah Nama\n 3. Ubah Umur\n 4. Ubah Alamat\n 5. Keluar")
    print("=" * 40)
    
    opsi = int(input("input opsi: "))
    
    if opsi == 1 :
        print("=" * 40)
        detail_pengguna()
    elif opsi == 2:
        mengubah_nama()
    elif opsi == 3:
        mengubah_umur()
    elif opsi == 4:
        mengubah_alamat()
    elif opsi == 5:
        print("=" * 40)
        print(f"Selamat Tinggal {data['Nama']}")
        break
    else:
        print("Opsi tidak valid. Silakan pilih opsi yang valid.")