def find_duplicates(array1, array2):
    duplicates = set(array1) & set(array2)
    return list(duplicates)

def main():
    input_array1 = input("Input array ke-1 (pisahkan angka dengan spasi): ").split()
    input_array2 = input("Input array ke-2 (pisahkan angka dengan spasi): ").split()

    # Konversi input ke tipe data integer
    array1 = [int(num) for num in input_array1]
    array2 = [int(num) for num in input_array2]

    # Cari duplikat
    duplicate_numbers = tuple(find_duplicates(array1, array2))

    if len(duplicate_numbers) > 0:
        print(f"Terdapat {len(duplicate_numbers)} buah duplikat yaitu {duplicate_numbers}")
    else:
        print("Tidak ada duplikasi ditemukan.")

# Panggil fungsi main langsung
main()