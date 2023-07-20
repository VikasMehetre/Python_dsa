def binarysearch_Recursive(A,key,L,R):
    if L>R:
        return "Not found"
    else :
        mid=(L+R)//2
        if key==A[mid]:
            return mid
        elif key>A[mid]:
            return binarysearch_Recursive(A,key,mid+1,R)
        elif key<A[mid]:
            return binarysearch_Recursive(A,key,L,mid-1)
    return-1
a=[56,32,67,986,44,32,78,234]
a.sort()
print(binarysearch_Recursive(a,44,0,len(a)-1))    