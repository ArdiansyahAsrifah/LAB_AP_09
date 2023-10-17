var = input("Masukkan kata : ")
tengah = len(var)//2

if len(var)%2 != 0:
    print(var[0]+var[tengah]+var[-1])
else:
    print(var[0]+var[tengah-1]+var[tengah]+var[-1])