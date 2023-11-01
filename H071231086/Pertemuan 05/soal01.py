def stringbaru(s1,s2):

    s3 = ""
    jk = min(len(s1),len(s2))

    for i in range(jk): 
        s3 += s1[i] + s2[-(i+1)]  
    s3 += s1[jk:] + s2[:-jk] 
    return s3


s1 = (input())
s2 = (input())
s3 = stringbaru(s1,s2)
print(s3)