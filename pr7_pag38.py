s=str(input())
print(s.count('A'),s.replace('A','*'),s.replace('B',''), sep='\n')
print(s.count('MA'),s.replace('MA','TA'),s.replace('TO',''),s[::-1], sep='\n')
if s[::-1]==s:
    print(True)
else:
    print(False)
print(s.upper())
s8=s
for i in range(0,len(s8)-1):
    if ord(s8[0])>=97 and ord(s8[0])<=122:
        d=s8[0]
        d=d.upper()
        s8=d+s8[1:]
    if (ord(s8[i])<65 or (ord(s8[i])>90 and ord(s8[i])<97) or ord(s8[i])>122) and (ord(s8[i+1])>=97 and ord(s8[i+1])<=122):
        d=s8[i+1]
        d=d.upper()
        s8=s8[:i+1]+d+s8[i+2:]
#s9='' #Ordine pur alfabetic
#for k1 in range(65,91):
#    k2=k1+32
#    e=s.count(chr(k1))
#    s9+=chr(k1)*e
#    e=s.count(chr(k2))
#    s9+=chr(k2)*e
s9="".join(sorted(s)) #Ordine ASCII
print(s8,s9,sep='\n')