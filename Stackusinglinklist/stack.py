class _Node:
    __slots__="_elemet","_next"
    def __init__(self,element,next):
        self._elemet=element
        self._next=next
class Stacklink:
    def __init__(self) :
        self._top=None
        self._size=0
    def __len__(self):
        return len(self._size)
    def isEmpty(self):
        return len(self._size)==0
    def push(self,e):
        newest=_Node(e,None)        
        if self.isEmpty():
            self._top=newest
        else:
            newest._next=self._top
            self._top=newest
        self._size+=1         
    def pop(self):
        if self.isEmpty():
            return "is Empty"
        e=self._top._elemet
        self._top=self._top._next
        self._size-=1
        return e
    def top(self):
        if self.isEmpty():
            return "is Empty"
        return self._top._elemet
    def display(self):
        p=self._top
        while p:
            print(p._elemet,end="=>")
            p=p._next
        print()    
       
S=Stacklink()      
S.push(4)
S.push(6)
S.push(8)
S.push(2)
S.push(9)
print(S.__len__())
S.display()
S.pop()
S.display()
print(S.__len__())
print(S.top())
