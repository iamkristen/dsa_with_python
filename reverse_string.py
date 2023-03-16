from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self,val):
        self.container.append(val) 
    
    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]
    
    def isEmpty(self):
        return self.container == 0
    
    def size(self):
        return len(self.container)
    
    def show(self):
        return self.container
    
if __name__ == "__main__":
    
    stack = Stack()
        
    def reverseString(val):
        for v in val:
            stack.push(v)
        result = ""
        while stack.size() != 0:
            result+= stack.pop()
        return result

    print(reverseString("We will conquere COVID-19"))

    
    