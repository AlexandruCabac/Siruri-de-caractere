a,b=str(input()),''
for i in range(0,len(a)):
    if a[i]==' ':
        b+='-'
    elif a[i]=='Z':
        b+='A'
    else:
        b+=chr(ord(a[i])+1)
print(b)