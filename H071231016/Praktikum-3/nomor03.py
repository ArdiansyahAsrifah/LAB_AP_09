while True:
    try:
        derajat = float(input("Masukkan nilai derajat : "))
        #Konversi Derajat ke satuan waktu
        total_detik = derajat * 240 + (6 * 3600) # 6 * 3600 itu maksudnya supaya formatnya jam 6 pagi
        total_detik = int(total_detik)  #Konversi agar dari float ke integer spy ndd koma
        #Jika total detiknya lebih dari sehari full maka kita kurangi lagi dengan 24 jam
        if total_detik >= (24 * 3600):
            total_detik = total_detik - (24 * 3600) #Agar terformat 24 jam 25 jam 01:00:00 
        jam = total_detik // 3600 #3600 detik =  1 jam
        menit = (total_detik % 3600) // 60 #3600 modulo 3600
        sisadetik = total_detik % 60

        if 6 <= jam < 12:
            print("Selamat Pagi")
        elif 12 <= jam < 15:
            print("Selamat Siang")
        elif 15 <= jam < 18:
            print("Selamat Sore")
        else:
            print("Selamat Malam")

        print(f"{jam:02}:{menit:02}:{sisadetik:02}")
        break #ini beda dengan break yg ada dibagian bawah
    except ValueError:
        print("End Of File")
        break