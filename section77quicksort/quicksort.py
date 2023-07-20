#worst case for quick sort is when the elemnts are already sorted 0(n^2)
#best is nlogn
def quicksort(a,low,high):
    if low<high:
        pi=partion(a,low,high)
        quicksort(a,low,pi-1)
        quicksort(a,pi+1,high)
    return a    
def partion(a,low,high):
    povit=a[low]
    i=low+1    
    j=high
    while True:
        while i<=j and a[i]<=povit:
            i=i+1
        while i<=j and a[j]>=povit:
            j=j-1
        if i<=j:
            a[i],a[j]=a[j],a[i]
        else:
            break
    a[low],a[j]=a[j],a[low]
    return j                    
arr=[54,36,98,72,12,25]
x=quicksort(arr,0,len(arr)-1)
print(x)

