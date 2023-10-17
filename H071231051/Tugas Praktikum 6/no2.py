def irisan(angka1, angka2):
    irisan = set(angka1) & set(angka2)
    if irisan:
        return f"Terdapat {len(irisan)} buah yaitu {irisan}"
    else:
        return "Tidak ada duplikasi ditemukan"
    
nilai1 = [int(x) for x in input('Input array ke-1: ').split()]
nilai2 = [int(x) for x in input('Input array ke-2: ').split()]
print(irisan(nilai1, nilai2))