import re

angka = int(input())
list_ip=[]
for i in range(angka):
    tes_ip = input()
    list_ip.append(tes_ip)
    
for i in range(len(list_ip)):
    if len(list_ip[i]) <= 500:
        ipv4 = re.search(r'^(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}$',list_ip[i])
        ipv6 = re.search(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$',list_ip[i])
        if ipv4:
            print('IPv4')
        elif ipv6:
            print('IPv6')
        else:
            print('Bukan IP Address')