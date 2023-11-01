def anagram(kata1, kata2):
    kata1 = kata1.replace(" ", "").lower()
    kata2 = kata2.replace(" ", "").lower()
    anagram = tuple(sorted(kata1)) == tuple(sorted(kata2))
    return anagram

kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

if anagram(kata1, kata2):
    print("True")
else:
    print("False")