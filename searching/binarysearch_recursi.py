def search(A, left, right, x):
    if left <= right: 
        mid = (left + right) // 2 

        if x == A[mid]:
            return 1
        elif x < A[mid]:  
            return search(A, left, mid - 1, x)
        else:  
            return search(A, mid + 1, right, x)
    else:
        return -1

A = [10, 20, 30, 40, 50, 60]
x = 770
left = 0
right = len(A) - 1
print(search(A, left, right, x))

"""
log2n will be time complexity even if the search is successful or un success """