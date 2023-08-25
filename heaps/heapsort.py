from heap import heaps
def heapsort(A):
    H = heaps(10)
    n = len(A)
    for i in range(n):
        H.insert(A[i])
    k = n-1
    for i in range(H._currsize):
        A[k] = H.delmax()
        k = k - 1
A = [63, 250, 835, 947, 651, 28]
print('Original Array:',A)
heapsort(A)
print('Sorted Array:',A)