kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

def anagram(kata1, kata2):

    kata1, kata2 =sorted(kata1.replace(" ", "").lower()), sorted(kata2.replace(" ", "").lower())
    if (kata1) != (kata2):
        return False
    
    return kata1 == kata2


print(anagram(kata1, kata2))