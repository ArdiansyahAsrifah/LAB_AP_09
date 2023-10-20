kata1 = input("Masukkan input pertama: ")
kata2 = input("Masukkan input kedua: ")

kata1 = kata1.lower().replace(" ","")
kata2 = kata2.lower().replace(" ","")

tuple_kata1 = sorted(kata1)
tuple_kata2 = sorted(kata2)

print(tuple_kata1)

anagram = tuple_kata1 == tuple_kata2
print(anagram)