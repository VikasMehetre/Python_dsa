A=[5,67,43,2,457,33,79,33,2]
def select(A):
    n=len(A)
    for i in range(n-1):
        postion=i
        for j in range(i+1,n):
            if A[j]<A[postion]:
                postion=j
        temp=A[i]
        A[i]=A[postion]  
        A[postion]=temp
        
    return A    
print(select(A))             
