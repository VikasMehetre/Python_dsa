class dequeue:
    def __init__(self):
        self._data=[]
        self._size=0
    def __len__(self):
        return len(self._data)   
    def isEmpty(self):
        return len(self._data)==0
    def addfirst(self,e):
        self._data.insert(0,e)
    def addlast(self,e):
        self._data.append(e)
    def remfirst(self):
        if self.isEmpty():
            return "empty"
        else:
            return self._data.pop(0)       
    def remlast(self):
        if self.isEmpty():
            return "is Empty"
        else:
            return self._data.pop()
    def first(self):
        if self.isEmpty():
            return "is Empty"
        return self._data[0]
    def last(self):
        if self.isEmpty():
            return "is Empty"
        return self._data[-1]
D=dequeue()
D.addfirst(3)
D.addfirst(8)
D.addfirst(2)
D.addlast(4)            
D.addlast(9)            
D.addlast(7)
print(D._data)   
print(D.first())         
print(D.last())
print(D.remfirst())
print(D._data)         
print(D.remlast())
print(D._data)         