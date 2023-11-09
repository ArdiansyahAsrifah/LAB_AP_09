import re

string = input()
if len(string) == 45:
    pattern = r"^[A-Za-z02468]{40}[13579\s]{5}$"

    if re.match(pattern, string):
        print(True)
    else:
        print(False)
else:
    print(False)