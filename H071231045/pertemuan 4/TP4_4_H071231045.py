def CatAndMouse(CatA, CatB, MouseC):
    a = (CatA - MouseC) 
    if a < 0:
        a = -(CatA-MouseC)
    b = (CatB - MouseC)
    if b < 0:
        b = -(CatB-MouseC)
        
    if a > b:
        print("Cat B")
    elif a < b:
        print("Cat A")
    elif a == b:
        print("Mouse C")


CatA = int(input("Masukkan Jarak Cat A : "))
CatB = int(input("Masukkan Jarak Cat B : "))
MouseC = int(input("Masukkan Jarak Mouse C : "))

CatAndMouse(CatA, CatB, MouseC) 