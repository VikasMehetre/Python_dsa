class _Node:
    __slots__="_element","_next"
    def __init__(self,element,next):
        self._element=element
        self._next=next
class Linklist:
    def __init__(self):
        self._head=None
        self.tail=None
        self._size=0
    def __len__(self):
        return self._size
    def isEmpty(self):
        if self._size==0:
            return True
        else :
            return  False
    def addlast(self,element):      
        newest=_Node(element,None)
        if self.isEmpty():
            self._head=newest
        else:
            self._tail._next=newest
        self._tail=newest
        self._size+=1
    def display(self):
        p=self._head
        while p:
            print(p._element,end='-->')
            p=p._next
        print()     
    def search(self,key):
        p=self._head
        index=0
        while p:
            if p._element==key:
                return index
            p=p._next
            index=index+1
        return -1 
    def insertbegin(self,element):
        newest =_Node(element,None)
        if self.isEmpty():
            self._head=newest
            self._tail=newest
        else:
            newest._next=self._head
            self._head=newest
        self._size+=1      
    def addat(self,element,position):
        newest=_Node(element,None)
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
            return "is Empty"
        e=self._head._element
        self._head=self._head._next
        self._size-=1
        if self.isEmpty():
            self._tail=None
        return e    
    def remend(self):
        if self.isEmpty():
            return "list is empty"
        p=self._head
        i=1
        while i< self.__len__()-1:
            p=p._next
            i=i+1
        self._tail=p
        p=p._next
        e=p._element
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
        self._size-=1
        return e
L=Linklist()
L.addlast(4)
L.addlast(6)
L.addlast(8)
L.addlast(2)
L.addat(45,4)
L.insertbegin(7)

L.display()
x=L.remfirst()
x1=L.remend()
print(x)
print(x1)
x2=L.remat(2)
print(x2)
L.display()
print(L.__len__())
print(L.search(8))