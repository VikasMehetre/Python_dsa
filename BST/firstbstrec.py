class _Node:
    __slots__ = '_element', '_left', '_right'

    def __init__(self, element, left=None, right=None):
        self._element = element
        self._left = left
        self._right = right

class BinarySearchTree:
    def __init__(self):
        self._root = None

    def rinsert(self,troot,e):
        if troot:
            if e < troot._element:
                troot._left = self.rinsert(troot._left,e)
            elif e > troot._element:
                troot._right = self.rinsert(troot._right,e)
        else:
            n = _Node(e)
            troot = n
        return troot

    def serach(self,key):
        troot=self._root
        while troot:
            if key==troot._element:
                return True
            elif key<troot._element:
                troot=troot._left
            else :
                troot=troot._right
        return False           
    def inorder(self,troot):
        if troot:
            self.inorder(troot._left)
            print(troot._element,end=' ')
            self.inorder(troot._right)
    def rsearch(self,troot,key):
        if troot:
            if troot._element==key:
                return True
            elif  key < troot._element:
                return self.rsearch(troot._left,key)
            else:
                return self.rsearch(troot._right,key)
        return False   

B = BinarySearchTree()
B._root= B.rinsert(B._root,50)
B.rinsert(B._root,30)
B.rinsert(B._root,80)
B.rinsert(B._root,10)
B.rinsert(B._root,40)
B.rinsert(B._root,60)
B.rinsert(B._root,90)
B.inorder(B._root)
x=B.serach(23)
if x:
    print("Element found")   
else:
    print("Not found")    
print(B.rsearch(B._root,70))
