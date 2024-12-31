n=int(input(" enter:"))
arr=[int(i) for i in input().split()]
i=0
while i<n:
    if arr[i]%2==0:
        arr.pop(i)
        n=n-1 
    if arr[i]%2!=0:
        i=i+1
print(arr)        
