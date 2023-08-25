class heaps:
    def __init__(self,n):
        self._maxsize=n
        self._data=[-1]*self._maxsize
        self._currsize=0
    def __len__(self):
        return len(self._data)
    def isEmpty(self):
        return len(self._data)==0
    def insert(self,e):
        if self._currsize==self._maxsize:
            return"No space"
        self._currsize+=1
        hi=self._currsize
        while hi>1 and e>self._data[hi//2]:
            self._data[hi]=self._data[hi//2]
            hi=hi//2
        self._data[hi]=e        
    def max(self):
        if self._currsize==0:
            return "Empty"
        return self._data[1]  
    def delmax(self):
        if self.isEmpty():
            return "Empty"
        e=self._data[1]
        self._data[1]=self._data[self._currsize]
        self._data[self._currsize]=-1
        self._currsize-=1
        i=1
        j=i*2
        while j<=self._currsize:
            if self._data[j]<self._data[j+1]:
                j=j+1
            if self._data[i] <self._data[j]:
                temp=self._data[i]
                self._data[i]=self._data[j]
                self._data[j]=temp
                i=j
                j=i*2
            else:
                break
        return e            
    
# S=heaps(10)
# S.insert(40)
# S.insert(20)
# S.insert(25)
# S.insert(14)
# S.insert(10)
# S.insert(2)
# print(S._data)     
# print(S.delmax())
# print(S._data)
     