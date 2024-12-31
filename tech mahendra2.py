n=int(input("entern:"))
arr=[int(i) for i in input().split()]
ev=0
od=0
count=0
i=0
for i in range(len(arr)):
    if i%2==0:
        ev=ev+arr[i]
    else: 
        od=od+arr[i]
    count=ev-od
print(ev)
print(od)
print(count)