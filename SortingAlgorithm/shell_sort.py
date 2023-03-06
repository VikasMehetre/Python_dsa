import math as m
def Shell(A):
    n=len(A)
    gap=n//2
    while gap>0:
        i=gap
        while i<n:
            gvalue=A[i]
            j=i-gap
            while j>=0 and A[j]>gvalue:
                A[j+gap]=A[j]
                j=j-gap
            A[j+gap]=gvalue
            i=i+1
        gap=gap//2    
    return A        
A=[3,6,2,4,7,9,1]
print(Shell(A))                
