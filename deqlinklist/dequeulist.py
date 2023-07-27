class _Node:
    __slots__="_element","_next"
    def __init__(self,element,next):
        self._element=element
        self._next=next
class DequeueLink:
    def __init__(self):
        self._front=None
        self._rear=None
        self._size=0
    def __len__(self):
        return self._size
    def isEmpty(self):
        return self._size==0     
    def addfirst(self,e):
        newest=_Node(e,None)
        if self.isEmpty():
            self._rear=newest
        newest._next=self._front
        self._front=newest
        self._size+=1    

    def addlast(self,e):
        newest=_Node(e,None)
        if self.isEmpty():
            self._front=newest
        self._rear._next=newest
        self._rear=newest
        self._size+=1
    def remfirst(self):
        if self.isEmpty():
            return "is Empty"
        e=self._front._element
        self._front=self._front._next
        self._size-=1
        return e
    def remlast(self):
        if self.isEmpty():
            return "is Empty"
        p=self._front
        i=1
        while i< self.__len__()-1:
            p=p._next
            i=i+1
        e=p._next._element
        p._next=None
        self._size-=1
        return e
    def display(self):
        p=self._front
        i=0
        while p:
            print(p._element,end="-->")
            p=p._next
        print()    
D=DequeueLink()
D.addfirst(4)            
D.addfirst(7)            
D.addfirst(8)
D.addlast(9)            
D.addlast(2)            
D.addlast(4)        
D.display()    
print("Size of Deque:", D.__len__() )
print(D.remfirst())
D.display()
print(D.remlast())
D.display()

         