import math
"""def see(A,x):
    if x in A:
        return 1
    return -1
A=[1,2,3,4,5,65,3,3,34,2,2,5,6,7,466,90]
x=99
print(see(A,x))
"""
def bst(A,x):
    l=len(A)
    high=l-1
    low=0
    while low <= high:
 
        mid = (high + low) // 2
 
        if A[mid] < x:
            low = mid + 1
 
        elif A[mid] > x:
            high = mid - 1
 
        else:
            return 1
 
    return -1
    
A=[10,20,30,40,50,60]
x=40
print(bst(A,x) )       
        
    
            

