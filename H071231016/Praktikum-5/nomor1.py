kata1 = input()
kata2 = input()
i = 0
balik = kata2[::-1]
kata3 = ""
while i < len(kata1) and i < len(kata2) :
    kata3 += kata1[i] + balik[i]
    i += 1
kata3 += kata1[i:] + balik[i:]
print(kata3)

