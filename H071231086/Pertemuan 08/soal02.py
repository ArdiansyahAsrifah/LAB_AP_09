import re

def check_ip_type(ip):
    if re.match(r'^(0|([1-9]\d?|1\d{2}|2[0-4]\d|25[0-5]))(\.(0|([1-9]\d?|1\d{2}|2[0-4]\d|25[0-5]))){3}$', ip):
        return "IPv4"
    elif re.match(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$', ip):
        return "IPv6"
    else:
        return "Bukan IP Address"

n = int(input())
for _ in range(n):
    ip = input()
    result = check_ip_type(ip)
    print(result)
