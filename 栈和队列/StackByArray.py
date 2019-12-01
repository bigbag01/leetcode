# coding=utf-8
# 用比较原始的方法在python list基础上实现stack

# 实际上python的list已经拥有了stack的功能，l.append(ele),l.pop(),l[-1],len(l),len(l)==0 分别对应栈的五个功能函数
class StackByArray:
    def __init__(self):
        self.store = []
        self.size = 0

    def pop(self):
        if self.size > 0:
            target = self.store[self.size-1]
            del self.store[self.size-1]
            self.size -= 1
            return target
        else:
            raise IndexError("pop from empty stack")

    def push(self,element):
        self.store.append(element)
        self.size += 1

    def peek(self):
        if self.size > 0:
            target = self.store[self.size-1]
            return target
        else:
            raise IndexError("peek from empty stack")

    def size(self):
        return self.size
        
    def isEmpty(self):
        return self.size == 0
    
myStack = StackByArray()
myStack.push(5)
myStack.push(3)
myStack.push(7)
print(myStack.peek())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
