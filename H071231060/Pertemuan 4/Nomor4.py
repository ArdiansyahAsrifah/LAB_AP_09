def CatAndMouse(catA, catB, mouseC):
    a = abs(catA - mouseC)
    b = abs(catB - mouseC)
    if a > b :
        print("catB")
    elif a < b :
        print("catB")
    else:
        print("mouseC")
result = CatAndMouse(catA=(int(input())), catB=(int(input())), mouseC=(int(input())))
print(result)