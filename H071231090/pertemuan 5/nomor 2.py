input_string = input("Masukkan string: ")

if len(input_string) < 3:
    print("Panjang string terlalu pendek.")
else:
    karakter_tengah = len(input_string) // 2

    new_string = input_string[0] + input_string[karakter_tengah] + input_string[-1]

    print("String baru:", new_string)