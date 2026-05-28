class MinStack:

    # def __init__(self):
    #     self.stack = []
    #     self.min_ = float('inf')

    # def push(self, val: int) -> None:
    #     self.stack.append(val - self.min_)
    #     self.min_ = min(val, self.min_)

    # def pop(self) -> None:
    #     popped = self.stack.pop()
    #     if popped < 0:
    #         self.min_ = self.min_ - popped

    # def top(self) -> int:
    #     if self.stack[-1] < 0:
    #         return self.min_    
    #     return self.stack[-1] + self.min_        

    # def getMin(self) -> int:
    #     return self.min_

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0 or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
