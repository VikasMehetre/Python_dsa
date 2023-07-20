def re(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*re(n-1)
    
print(re(5))