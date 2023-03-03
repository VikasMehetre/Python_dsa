def leaer(A):
    n=len(A)
    list_1=[]
    cvalue=A[n-1]
    for i in range(n-2,0,-1):
        if A[i]>cvalue:
            list_1.append(A[i])
            print(A[i])
    print(list_1)            
            
A=[3,4,62,3,5,8,9]
leaer(A)                