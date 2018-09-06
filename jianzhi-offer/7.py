# coding: utf-8

# 用两个栈实现一个队列

class StackQueue():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def add(self, val):
        self.stack1.append(val)

    def pop(self):
        assert len(self.stack1) + len(self.stack2) > 0, 'No value to pop'
        if len(self.stack2) == 0:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        return self.stack2.pop()
