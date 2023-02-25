list_1=[12,45,33,75,97,34,67,45]
list_1=list_1.sort
value_found=int(input("Enter the value to be found inthe list"))
n=len(list_1)
i=0
j=n
for x in list_1:
    mid=n/2
    if value_found == mid:
        print("Statement found")
    elif value_found<mid :
        j=mid-1
    else :
        i=mid+1       
    