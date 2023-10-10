def maksimum(x):
    maksimum = x[0]
    for i in x:
        if maksimum < i:
            maksimum = i
    return maksimum
x = input('Masukkan daftar angka: ')
x = [int(maksimum) for maksimum in x.split(",")]
# x = (0, 1, 3, 5, 2, 6, 4, 7, 8, 1, 5)
print(maksimum(x))
