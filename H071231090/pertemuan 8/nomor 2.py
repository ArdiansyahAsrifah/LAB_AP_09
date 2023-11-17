import re

jumlah_inputan = int(input())

list_karakter = []
for i in range(jumlah_inputan):
    karakter = input()
    list_karakter.append(karakter)

def ip_address(pattern):
    Ipv4 = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$" 
    Ipv6 = r"^([0-9a-fA-F]{1,4}\:){7}[0-9a-fA-F]{1,4}$"
    for i in pattern:
        if re.match(Ipv4, i):
            print("IPv4")
        elif re.match(Ipv6, i):
            print("IPv6")
        else:
            print("Bukan IP Address")

ip_address(list_karakter)