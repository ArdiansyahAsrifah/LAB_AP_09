def maksimum(*a):
    angka_terbesar = a[0]
    for angka in a:
        if angka > angka_terbesar:
            angka_terbesar = angka
    return angka_terbesar

angka1 = maksimum(int(input()))
print(angka1)