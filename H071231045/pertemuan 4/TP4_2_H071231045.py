def palindrom(x):
    if x.lower() == x[::-1].lower(): #slicing
        print("Palindrom")
    else:
        print("Bukan Palindrom")
palindrom("apa")