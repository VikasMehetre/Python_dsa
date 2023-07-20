class _Node:
    __slots__="_element","_next"
    def __init__(self,elemet,next):
        self._element=elemet
        self._next=next
n1=_Node(7,None)
n2=_Node(4,None)     
#creating an link
n1._next=n2   
print(n1._element,n2._element)
print(n1._next)