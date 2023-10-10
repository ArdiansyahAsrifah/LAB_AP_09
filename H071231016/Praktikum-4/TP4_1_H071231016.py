def geserhuruf(n): 
    for i in range(len(n)):
        n = n[-1] + n [:-1] 
        print(n, end=" | ")
try:
    geserhuruf("Mobil")
except TypeError:
    print("Terjadi error, n harus bertipe data string")


