n=int(input("enter the integer:"))
if n%3==0 and n%5==0:
    print("fizzbuzz")
if n%3==0 and n%5!=0:
    print("fizz")
if n%5==0 and n%3!=0:
    print("buzz")
if n%5!=0 and n%3!=0:
    print("buzzfizz")            