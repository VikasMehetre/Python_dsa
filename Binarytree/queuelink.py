class _Node:
    __slots__="_element","_next"
    def __init__(self,element,next):
        self._element=element
        self._next=next
class queuelink:
    def __init__(self) :
        self._front=None
        self._rear=None
        self._size=0
    def __len__(self):
        return    self._size
    def isEmpty(self):
        return self._size==0
    def enqueue(self,e):
        newest=_Node(e,None)
        if self.isEmpty():
            self._front=newest
        else:
            self._rear._next=newest
        self._rear=newest
        self._size+=1
    def dequeue(self):
        if self.isEmpty():
            return "is Empty"
        e=self._front._element
        self._front=self._front._next
        self._size-=1
        if self.isEmpty():
            self._rear=None
        return e
    def first(self):
        if self.isEmpty():
            return "is Empty"    
        return self._front._element
    def display(self):
        p=self._front
        while p:
            print(p._element,end="-->")
            p=p._next
        print()
Q=queuelink()
Q.enqueue(5)            
Q.enqueue(8)            
Q.enqueue(9)            
Q.enqueue(3)
Q.display()
print(Q.__len__())
print(Q.isEmpty())
print(Q.dequeue())
Q.display()
print(Q.first())
Q.display()

