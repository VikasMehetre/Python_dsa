def bubble(A):
    n=len(A)
    for i in range(n-1,0,-1):
        for j in range(i):
            if A[j]>A[j+1]:
                temp=A[j]
                A[j]=A[j+1]
                A[j+1]=temp
    return A
A=[23,56,221,67,5,5,75,21]
print(bubble(A))            