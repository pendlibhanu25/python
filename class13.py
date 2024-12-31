arr=[]
x = int(input())
y = int(input())
z = int(input())
n = int(input())
i=0
j=0
k=0
if i<=x+1:
    i=i+1
    if j<=y+1:
        j=j+1
        if k<=z+1:
            k=k+1
            if i+j+k!=3:
               arr.append([i,j,k])
print(arr)   
                
        
        
        