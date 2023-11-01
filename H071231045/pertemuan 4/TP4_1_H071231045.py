def geserhuruf(n):
    for i in range(len(n)):
        n = n[-1]+ n[:-1]
        print(n, end=" | ")

try:
    geserhuruf('MOBIL')
except TypeError:
    print("Terjadi error, N harus bertipe data string")
