def maxdiff(a):
    n=len(a)
    m=a[0]
    x=a[n-1]
    for i in range(1,n-1):
        if(a[i]>x):
            x=a[i]
        if(a[i]<m):
            m=a[i]
    print(x-m)
A=[6,5,2,9,10,56,24]    
maxdiff(A)                