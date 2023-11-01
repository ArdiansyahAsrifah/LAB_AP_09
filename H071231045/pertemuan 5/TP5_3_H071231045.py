def anagram(kata1, kata2):
    kesalahan = 0
    kata1 = kata1.replace(" ","").lower()
    kata2 = kata2.replace(" ","").lower()

    for huruf in kata1:
        cek1 = kata1.count(huruf)
        cek2 = kata2.count(huruf)
        if cek1 != cek2 :
            kesalahan += 1

    if kesalahan == 0 and len(kata1) == len(kata2):
        return True
    else:
        return False

kata1 = input("Masukkan kata pertama : ")
kata2 = input("Masukkan kata kedua : ")
 
print(f"2 kata adalah Anagram = {anagram(kata1,kata2)}") 