s1=input('s1 = ')
s2=input('s2 = ')[::-1]
x=(min(len(s1),len(s2)))
hasil=''

for i in range(x):
    hasil=hasil+s1[i]+s2[i]

if len(s1)>len(s2):
    hasil=hasil+s1[x:]
elif len(s2)>len(s1):
    hasil=hasil+s2[x:]
    
print(f'Hasil Mixed ="{hasil}"')