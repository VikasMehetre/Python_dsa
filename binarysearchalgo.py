import math as m
def binary(A,key):
    n=len(A)
    L=0
    R=n-1
    while L<R:
        mid=m.floor((L+R)/2)
        if key==A[mid]:
            return mid
        elif key>A[mid]:
            L=mid+1
        else :
            R=mid-1
    return -1
list_u=[23,56,3,22,5,3,2,45,22,113,45]
list_u.sort()
print(list_u)
print(binary(list_u,56))