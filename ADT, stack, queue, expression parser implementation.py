class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None  # Return None if stack is empty
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None  # Return None if stack is empty
    
    def size(self):
        return len(self.items)

# Example usage:
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.pop())  # Output: 30
print(stack.peek())  # Output: 20
print(stack.size())  # Output: 2
