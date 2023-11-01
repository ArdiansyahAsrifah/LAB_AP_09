def Palindrom(kata: str) -> str:
    kata = kata.lower()
    if kata == kata [::-1]:
        print("Palindrom")
    else:
        print("Bukan Palindrom")

Palindrom(input())