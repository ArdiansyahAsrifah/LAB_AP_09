import re

string = input()
match = re.search(r'^[A-z02468]{40}[13579\s]{5}$',string)
if match:
    print(True)
else:
    print(False)