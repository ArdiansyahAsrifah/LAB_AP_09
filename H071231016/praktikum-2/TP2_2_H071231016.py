input_1 = str(input("Masukkan Input Pertama :")).lower()
input_2 = str(input("Masukkan Input Kedua   :")).lower()
input_3 = str(input("Masukkan Input Ketiga  :")).lower()

match input_1, input_2, input_3:
    case "vertebrado", "ave", "carnivoro":
        hasil = "agula"
    case "vertebrado", "ave", "onivoro":
        hasil = "pomba"
    case "vertebrado", "mamifero", "onivoro":
        hasil = "homem"
    case "vertebrado", "mamifero", "herbivoro":
        hasil = "vaca"
    case "invertebrado", "inseto", "hematofago":
        hasil = "pulga"
    case "invertebrado", "inseto", "herbivoro":
        hasil = "lagarta"
    case "ivertebrado", "anelideo", "hematofago":
        hasil = "sanguessuga"
    case "invertebrado","anelideo", "onivoro":
        hasil = "minhoca"
    case _ :
        hasil = "Invalid Input"
        
print (hasil)
