def Permutasi(kata):
    try:
        pangjang_kata = len(kata)
        for i in range (pangjang_kata):
            kata = kata[-1:] + kata[:-1]
            print(kata, end= " | ")
    except TypeError:
        print("input harus berupa string")
Permutasi(input())