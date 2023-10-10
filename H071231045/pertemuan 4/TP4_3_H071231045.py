def terbesar(*x): #ars
    terbesar = x[0]
    for i in x:
        if terbesar < i:
            terbesar = i
    return terbesar

print(terbesar(0, 2, 1, 3, 5, 2, 6, 4, 7, 8, 1, 5))

print('\n======cara kedua======')
while True:
    x = int(input("Jumlah item = "))
    nums = []
    for i in range(x):
        y = int(input("Angka = "))
        nums.append(y)
        i -=1
    print(terbesar(*nums))
    break