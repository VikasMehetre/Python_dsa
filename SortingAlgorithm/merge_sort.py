import math as m
def mergesort(a,left,right):
    if left < right:
        mid=m.floor((left+right)/2)
        mergesort(a,left,mid)
        mergesort(a,mid+1,right)
        merge(a,left,mid,right)
    return a    
def merge(a,left,mid,right):
    i=left
    j=mid+1
    k=left
    b=[0]*(right+1)
    while i<=mid and j<=right:
        if a[i]<a[j]:
            b[k]=a[i]
            i+=1
            k=k+1
        else:
            b[k]=a[j]
            j=j+1
            k=k+1
    while i<=mid:
        b[k]=a[i]
        i=i+1
        k=k+1
    while j<=right:
        b[k]=a[j]
        j=j+1
        k=k+1
    for m in range(left,right+1):
        a[m]=b[m]
    return a                
    
A=[34,3,6,45,78,4,5,1,9]       
x=mergesort(A,0,len(A)-1)
print(x)     
  
                