# -*- coding:utf-8 -*-
# 用单链表实现栈

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class StackByLinkedList:
    def __init__(self):
        self.store = None
        self.size = 0

    def push(self,element):
        head = ListNode(element)
        head.next = self.store
        self.store = head
        self.size += 1

    def pop(self):
        if self.store == None:
            raise IndexError("pop from empty stack")
        else:
            cur = self.store
            top_val = cur.val
            self.store = self.store.next
            del cur
            self.size -= 1
            return top_val

    def peek(self):
        if self.store == None:
            raise IndexError("peek from empty stack")
        else:
            return self.store.val

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

myStack = StackByLinkedList()
myStack.push(5)
myStack.push(3)
myStack.push(7)
print(myStack.peek())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.peek())