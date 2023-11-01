s1 = input("")
s2 = input("")
def karakter(s1, s2):
    s2 = s2[::-1]
    panjang = min(len(s1), len(s2))
    s3 = ''.join([s1[i] + s2[i] for i in range(panjang)])
    s3 += s1[panjang:] + s2[panjang:]
    return s3
print(karakter(s1, s2))
