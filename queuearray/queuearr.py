class queuearr:
    def __init__(self):
        self._data=[]
        self._size=0
    def __len__(self):
        return len(self._data)
    def isEmpty(self):
        return len(self._data) == 0
    def enequeue(self,e):
        self._data.append(e)
        self._size+=1
    def dequeue(self):
        if self.isEmpty():
            return "is Empty"
        else:
            e=self._data[0]
            self._data.pop(0)
            self._size-=1
            return e     
    def fisrt(self):
        if self.isEmpty():
            return "is Empty"
        else:
            return self._data[0]

Q=queuearr()
Q.enequeue(40)        
Q.enequeue(9)        
Q.enequeue(43)
print(Q._data)   
print(Q.dequeue())
print(Q._data)     
print(Q.fisrt())
            