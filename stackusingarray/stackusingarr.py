class StackArray:
    def __init__(self):
        self._data=[]
    def __len__(self):
        return len(self._data)
    def isEmpty(self):
        return  len(self._data) == 0
    def push(self,e):
        self._data.append(e) 
    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        else: 
          return self._data.pop()      
    def top(self):
        if self.isEmpty():
            return "Is Empty"
        else:
            return self._data[-1]
S=StackArray()
S.push(4)            
S.push(3)            
S.push(7)            
S.push(9)
print(S._data)
print(S.pop())
print(S._data)
print(S.top())
print(S.__len__())
print(S.isEmpty())
