import _heapq as heap
L1=[]
heap.heappush(L1,25)
heap.heappush(L1,20)
heap.heappush(L1,10)
heap.heappush(L1,14)
heap.heappush(L1,2)
print(L1)
e=heap.heappop(L1)
print(e)
print(L1)
e=heap.heappushpop(L1,35)
print(e)
print(L1)
L1=[2, 10,33,45, 20,14,25]
print(L1)
heap.heapify(L1)
print(L1)