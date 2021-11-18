class Stack:
    def __init__(self):
        self.__stk = []
        
    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        super().__init__()
        self.counter = 0

    def get_counter(self):
        return self.counter

    def pop(self):
        value = super().pop()
        self.counter = value + 1
    

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())