class MinStack:

    def __init__(self):
        self.stack = []
        self.min_v = None
    def push(self, val: int) -> None:
        if self.min_v == None:
            self.stack.append(0)
            self.min_v = val
        else:
            self.stack.append(val-self.min_v)
            self.min_v = min(self.min_v,val)
        
        

    def pop(self) -> None:
        if self.stack[-1] < 0:
            self.min_v -= self.stack[-1]
        self.stack.pop()
        if len(self.stack) == 0:
            self.min_v = None
    def top(self) -> int:
        if self.min_v == None:
            return 0
        return self.min_v + max(0,self.stack[-1])

    def getMin(self) -> int:
        if self.min_v == None:
            return 0
        return self.min_v
