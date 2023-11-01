kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")
eror = 0

for i in kata1:
    pertama = kata1.count(i)
    kedua = kata2.count(i)
    if pertama != kedua:
        eror += 1
if eror == 0 and len(kata1) == len(kata2):
    print("true")
else:
    print("false")