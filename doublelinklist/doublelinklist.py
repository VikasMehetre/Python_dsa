class _Node:
    __slots__="_element","_next","_prev"
    def __init__(self,element,next,prev):
        self._element=element
        self._next=next
        self._prev=prev
class doublylinklist:
    def __init__(self):
        self._head=None
        self._tail=None
        self._size=0
    def __len__(self):
        return self._size
    def isEmpty(self):
        return self._size==0
    def addlast(self,e):
        newest=_Node(e,None,None)
        if self.isEmpty():
            self._head=newest
            self._tail=newest
        else :
            self._tail._next=newest
            newest._prev=self._tail
            self._tail=newest
        self._size+=1
    def display(self):
        if self.isEmpty():
            return "Is Empty"
        p=self._head
        while p:
            print(p._element,end="-->")
            p=p._next
    def displayrev(self):
        if self.isEmpty():
            return "is Empty"
        else:
            p=self._tail
            while p:
                print(p._element,end="-->")
                p=p._prev
    def addfirst(self,e):
        newest=_Node(e,None,None)
        if self.isEmpty():
            self._head=newest
            self._tail=newest
        else:
            newest._next=self._head
            self._head._prev=newest
            self._head=newest
        self._size+=1 
    def addat(self,e,position):
        newest=_Node(e,None,None)
        p=self._head
        i=1
        while i<position -1:
            p=p._next
            i=i+1
        newest._next=p._next
        p._next._prev=newest
        p._next=newest
        newest._prev=p
        self._size+=1   
    def rembeg(self):
        if self.isEmpty():
            return "is Empty"
        e=self._head._element
        self._head=self._head._next
        self._head._prev=None
        self._size-=1
        if self.isEmpty():
             self._tail=None# why not head ==noe casue it is done in line 67
        return e  
    def remend(self):
        if self.isEmpty():
            return "is Empty"
        e=self._tail._element
        self._tail=self._tail._prev
        self._tail._next=None
        self._size-=1
        return e      
    def remat(self,position):
        p=self._head
        i=1
        while i<position-1:
            p=p._next
            i=i+1
        e=p._next._element    
        p._next=p._next._next
        p._next._prev=p
        self._size-=1
        return e

D=doublylinklist()
D.addlast(4)                
D.addlast(6)                
D.addlast(67)                
D.addlast(43)
D.display()
D.addfirst(445)
print()
D.display() 
print()
D.addat(434,4)
print()
D.display
x=D.rembeg()
print(x)
D.display()
print()
x2=D.remend()
print(x2)
D.display()
x3=D.remat(3)
print()
print("elemt at position 3",x3)
D.display()
D.displayrev()           

 