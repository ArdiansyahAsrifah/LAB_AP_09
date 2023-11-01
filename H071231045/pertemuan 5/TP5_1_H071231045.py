def mix(var1, var2):
    var = ""
    var1 = kata1.replace(" ","")
    var2 = kata2[::-1].replace(" ","")

    pendek = min(len(var1), len(var2))

    for i in range(pendek):
        var += var1[i]
        var += var2[i]
    var += var1[pendek:] + var2[pendek:]
    return var

kata1 = input("Masukkan kata pertama : ")
kata2 = input("Masukkan kata kedua : ")

print(f"Hasil : {mix(kata1,kata2)}")
 