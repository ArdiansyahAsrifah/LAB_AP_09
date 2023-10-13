def stringbaru(karakter):
    jumlahHuruf = len(karakter)

    if jumlahHuruf < 3:
        return "string terlalu pendek"
    
    stringTerbaru = karakter [0] + karakter[jumlahHuruf//2] + karakter[-1]
    return stringTerbaru

string = input().replace(" ", "")
print(stringbaru(string))