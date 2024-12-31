n=int(input("entern:"))
arr=[int(i) for i in input().split()]
ev=0
od=0
count=0
i=0
for n in arr:
    if n%2==0:
        ev=ev+1
    else: 
        od=od+1
    count=ev-od
print(ev)
print(od)
print(count)