def sum(n,k):
    if n>0:
        k=k+n
        sum(n-1,k)
    else:
        print(k)    
(sum(6,0))        
def ss(n):
    if n>1:
        return ss(n-1)+n
    elif n==1:
        return 1
    else:
        print("done")
print(ss(5))        