from queuelink import queuelink
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
    def count(self,troot):  
        if troot:
            x=self.count(troot._left)
            y=self.count(troot._right)
            return x+y+1
        return 0 
    def height(self,troot):
        if troot:
            x=self.height(troot._left)       
            y=self.height(troot._right)
            if (x>y):
                return x+1
            else:
                return y+1
        return 0       
    def levelord(self):
        Q=queuelink()
        t=self._root
        print(t._element,end=" ")
        Q.enqueue(t)
        while not Q.isEmpty():
            p=Q.dequeue()
            if p._left :
                print(p._left._element,end=" ")
                Q.enqueue(p._left)
            if p._right:
                print(p._right._element,end=" ")
                Q.enqueue(p._right)                    

x=BinaryTree()
y=BinaryTree()
z=BinaryTree()
r=BinaryTree()
s=BinaryTree()
t=BinaryTree()
a=BinaryTree()
x.maketree(40,a,a)
y.maketree(60,a,a)
t.maketree(50,a,y)
r.maketree(20,x,a)
s.maketree(30,t,a)
z.maketree(10,r,s)
z.inorder(z._root)
print()
z.postorder(z._root)
print()
z.preorder(z._root)
print()
z.levelord()
print()
print(z.count(z._root))