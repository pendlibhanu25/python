a=input()
c=""
for i in a:
    if i>='97'and i<='122':
       c=c+chr(ord(i)-32)
    else:
        c=c+i
print(c)
        
