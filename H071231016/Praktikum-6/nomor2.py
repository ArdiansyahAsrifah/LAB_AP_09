a1 = set(map(int,(input("Masukkan array ke-1: ").split())))
a2 = set(map(int,(input("Masukkan array ke-2: ").split())))

x = a1.intersection(a2)
xtuple = tuple(x)
p = len(xtuple)
if p > 1:
    print(f"Terdapat {p} buah duplikat yaitu {xtuple}")
elif p == 1:
    print(f"Terdapat {p} buah duplikat yaitu ({xtuple[0]})")
else:
    print(f"Tidak ada duplikasi ditemukan.")
