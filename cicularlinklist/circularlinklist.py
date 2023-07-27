class _Node:
    __slots__="_element","_next"
    def __init__(self,element,next):
        self._element=element
        self._next=next
class circularlinklist:
    def __init__(self):
        self._head=None
        self._tail=None
        self._size=0
    def __len__(self):
        return self._size
    def isEmpty(self):
        return self._size==0
    def addlast(self,e):
        newest=_Node(e,None) 
        if self.isEmpty():
            newest._next=newest
            self._head=newest
        else:
            newest._next=self._tail._next
            self._tail._next=newest
        self._tail=newest
        self._size+=1
    def display(self):
        p=self._head
        i=0
        while i<self.__len__():
            print(p._element,end="-->")
            p=p._next
            i=i+1
    def atbegin(self,e):
        newest=_Node(e,None)
        if self.isEmpty():
            newest._next=newest
            self._head=newest
            self._tail=newest
        else:
            newest._next=self._head
            self._head=newest
            self._tail._next=newest    
        self._size+=1
    def addat(self,e,position):
        newest=_Node(e,None)
        p=self._head
        i=1
        while i<position-1:
            p=p._next
            i=i+1
        newest._next=p._next
        p._next=newest
        self._size+=1 
    def remfirst(self):
        if self.isEmpty():
            return"Empty"
        e=self._head._element
        self._tail._next=self._head._next
        self._head=self._head._next
        if self.isEmpty():
            self._head=None
            self._tail=None
        self._size-=1
        return e    
    def remend(self):
        if self.isEmpty():
            return "Empty"
        p=self._head
        i=1
        while i<self.__len__()-1:
            p=p._next
            i=i+1
        self._tail=p
        p=p._next
        self._tail._next=self._head
        e=p._element
        self._size-=1
        return e    
    def remat(self,position):
        if self.isEmpty():
            return "emeprt"
        p=self._head
        i=1
        while i<position-1:
            p=p._next
            i=i+1
        e=p._next._element
        p._next=p._next._next#path has been changed
        self._size-=1
        return e


C=circularlinklist()
C.addlast(5)    
C.addlast(4)    
C.addlast(7)    
C.addlast(8)
C.atbegin(34)
C.atbegin(4)
C.addat(45,3)
C.display()
print()
x=C.remfirst()
print("first element",x)
x1=C.remend()
print("rem end",x1)
print()
x2=C.remat(3)
print('removed at position 3:', x2 )
C.display()    

