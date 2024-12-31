li=[1,2,2,3,1,4,5,5,66,88,66,99,55]
dup_li=[]
un_li=[]
for i in li:
    if i not in un_li:
        un_li.append(i)
    elif i not in dup_li:
      dup_li.append(i)
print(f"unique eles {un_li}")
print(f"dup eles {dup_li}")
