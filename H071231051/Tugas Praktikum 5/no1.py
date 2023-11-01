def mixKarakter(s1, s2):
    s3 = []
    string1 = len(s1)
    string2 = len(s2)
    maksimal = max(string1, string2)

    for i in range(maksimal):
        if i < string1:
            s3.append(s1[i])
        if i < string2:
            s3.append(s2[-(i+1)])

    return "".join(s3)

s1 = input()
s2 = input()
print(mixKarakter(s1, s2))