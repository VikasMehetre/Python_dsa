def fac(n):
    if n==1:
        print("at 1")
        return 1
    elif n==0:
        print("at 0")
        return 1
    else:
        return fac(n-1)*n
print(fac(9))    
n=1
for i in range(10):
    if i==0:
        continue
    n=n*i
    print(n)

print(n)
