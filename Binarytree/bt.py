from typing import Any


class _Node:
    __slots__="_element","_left","_right"
    def __init__(self,element,left=None,right=None):
        self._element=element
        self._left=left
        self._right=right

class BinaryTree:
    def __init__(self):
        self._root=None
    def maketree(self,e,left,right):
        self._root=_Node(e,left._root,right._root)
    def preorder(self,troot):
        if troot:
            print(troot._element,end="-->")
            self.preorder(troot._left)
            self.preorder(troot._right)
    def inorder(self,troot):
        if troot:
            self.inorder(troot._left)
            print(troot._element,end="-->")
            self.inorder(troot._right)
    def postorder(self,troot):
        if troot:
            self.postorder(troot._left)                        
            self.postorder(troot._right)
            print(troot._element,end="-->")


x=BinaryTree()
y=BinaryTree()
z=BinaryTree()
a=BinaryTree()
x.maketree(10,a,a)
y.maketree(20,a,a)
z.maketree(30,x,y)
z.inorder(z._root)
print()
z.postorder(z._root)
print()
z.preorder(z._root)