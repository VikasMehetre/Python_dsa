import math as m
def mergesort(A,left,right):
    n=len(A)
    if right>left:
        mid=m.floor((left+right)/2)
        mergesort(A,left,mid)
        mergesort(A,mid+1,right)
        merge(A,mid,left,right)
    return A            
def merge(A,mid,left,right):
    i=left
    j=mid+1
    k=left
    while i<=mid and j<=right:
        if A[i]<A[j]:
            A[k] =A[i]
            k=k+1
            i=i+1
        else :
            A[k]=A[j]
            k=k+1
            j=j+1
A=[4,5,7,4,9,3,8,5]
n=len(A)
print(mergesort(A,0,n-1))        




    

