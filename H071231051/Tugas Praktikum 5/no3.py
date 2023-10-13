def anagram (karakter1, karakter2):
    karakter1 = karakter1.replace(" ","").lower()
    karakter2 = karakter2.replace(" ","").lower()
    
    if len(karakter1) != len(karakter2):
        return False

    char1 = {}
    char2 = {}

    for karakter in karakter1:
        if karakter in char1:
            char1[karakter] += 1
        else:
            char1[karakter] = 1
    
    for karakter in karakter2:
        if karakter in char2:
            char2[karakter] += 1
        else:
            char2[karakter] = 1
    
    return char1 == char2

kata1 = input()
kata2 = input()
print(anagram(kata1, kata2))
