input_1 = input("Input array ke-1: ").split()
input_2 = input("Input array ke-2: ").split()

set_1 = set(input_1)
set_2 = set(input_2)

duplikat = set_1 & set_2

if len(duplikat) > 0:
    print(f"Terdapat {len(duplikat)} buah duplikat yaitu {tuple(duplikat)}")
else:
    print("Tidak ada duplikasi ditemukan.")