"""def search(A,x):
    for i in range(len(A)):
        if A[i]==x:
            return i
        return -1
print(search([1,1,10,10,20,20,40],20))
"Time complexity in O(n)"""
def see(A,x):
    right=len(A)-1
    left=0
    while left<=right:
        mid=(left+right)//2
        if A[mid]==x:
            if A[mid-1]==x:
                return mid-1
            return mid 
        elif x>A[mid]:
            left=mid+1
        else:
            right=mid-1
    return -1
print(see([1,1,10,10,20,20,40],20))
print(see([5,10,10,15,20,20,20],20))    
