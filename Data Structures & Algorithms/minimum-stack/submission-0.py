class MinStack:

    def __init__(self):
        self.stack = []
        self.minList = []
        self.topIndex = -1
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        
        
        if (not self.minList):
            self.minList.append(val)
        else:
            if val < self.minList[self.topIndex]:
                self.minList.append(val)
            else:
                self.minList.append(self.minList[self.topIndex])
        
        self.topIndex += 1

    def pop(self) -> None:
        del self.stack[self.topIndex]
        del self.minList[self.topIndex]
        self.topIndex -= 1
        

    def top(self) -> int:
        return self.stack[self.topIndex]
        

    def getMin(self) -> int:
        return self.minList[self.topIndex]
        
