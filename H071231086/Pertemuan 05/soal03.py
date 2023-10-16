def are_anagrams(word1, word2):
    word1 = word1.lower().replace(" ", "")
    word2 = word2.lower().replace(" ", "")
    anagram = tuple(sorted(word1)) == tuple(sorted(word2))
    return anagram

word1 = input()
word2 = input()
hasil = are_anagrams(word1,word2)
print(hasil)