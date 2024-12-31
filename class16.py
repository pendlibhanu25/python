def factorial(n):
    if n==0:
        return 1
    return  factorial((n)+(n-1))
print(factorial())