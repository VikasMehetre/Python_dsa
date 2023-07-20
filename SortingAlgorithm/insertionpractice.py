def insert(arr):
    for i in range(1,len(arr)):
        cvalue=arr[i]
        position=i
        while arr[position-1]>cvalue  and position>0:
            arr[position]=arr[position-1]
            position=position-1
        arr[position]=cvalue
    return arr  
A=[34,3,6,45,78,4,5,1,9]            

x=insert(A)   
print(x)
#better to use when most of the elemnts are in the sorted order
