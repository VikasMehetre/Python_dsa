"""lisy_1=[1,23,45,32,134]
new_list=[x for x in lisy_1 if x%2==0 ]
print(new_list)
list_2=["vikas","Mehetre","5020130","IT"]
new_list_2=[x if x != "vikas" else "banana" for x in list_2 ]

print(new_list_2)"""
def functionll(A,n,key):
    index=0
    while n >index:
        if A[index]==key:
            return index
        index+=1
    return -1
print(functionll([64,674,3,45,78,5,43,234],8,234))
lsit=[64,674,3,45,78,5,43,234]
keyvalue=23
new_list=[x-keyvalue for x in lsit if x>keyvalue ]
print(new_list)
"""key_value=[x   for x in range(len(lsit)) if lsit[x]==5 ]
"""
