n = int(input("Masukkan jumlah suku Fibonacci: "))

if n < 0:
    print("Fibonacci tidak bisa kurang dari 0:")
elif n == 1:
    print(0)
else:
    u1 = 0
    u2 = 1
    print(u1, u2, end=" ")
    for i in range (n-2): #agar suku 1 dan 2 tidak diprint lagi
        u3 = u1 + u2
        u1, u2 = u2, u3 #definisikan ulang nilai u1 n u2 nya
        print(u3, end=" ")