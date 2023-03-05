def insert_sort(A):
    n=len(A)
    for i in range(1,n):
        cvalue=A[i]
        position=i
        while position>0 and A[position-1]>cvalue:
            A[position]=A[position-1]
            print("insisde loop before decremnetation",position)
            position=position-1
            print("after decrementation inside for loop ",position)
        print("outside whilw loop",position)    
        A[position]=cvalue
    return A    


A=[34,3,6,45,78,4,5,1,9]            
print(insert_sort(A))