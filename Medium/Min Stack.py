class MinStack(object):

    #  Last-In/First-Out (LIFO)
    def __init__(self):
        self.stack = []
        self.minStack = []
    def push(self, val):
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        # compare current val with the minstack, push if it smaller, ignore if isn't
        else:
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]
        return -1

    def getMin(self):
        if self.minStack:
            return self.minStack[-1]
        return -1


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # Output: -3
minStack.pop()
print(minStack.top())     # Output: 0
print(minStack.getMin())  # Output: -2