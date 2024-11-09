class Stack:
    def __init__(self):
        self.stack = []  # The stack is implemented using a list (array)

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def push(self, item):
        """Push an item onto the stack."""
        self.stack.append(item)

    def pop(self):
        """Pop an item from the stack."""
        if not self.is_empty():
            return self.stack.pop()  # Remove the last item (top of the stack)
        else:
            return "Stack is empty!"  # Return a message if the stack is empty

    def peek(self):
        """Peek at the top item of the stack."""
        if not self.is_empty():
            return self.stack[-1]  # Return the last item (top of the stack)
        else:
            return "Stack is empty!"  # Return a message if the stack is empty

    def size(self):
        """Return the size of the stack."""
        return len(self.stack)

    def display(self):
        """Display all items in the stack."""
        if not self.is_empty():
            print("Stack:", self.stack)
        else:
            print("Stack is empty.")

# Example usage:
stack = Stack()

# Pushing items onto the stack
stack.push(10)
stack.push(20)
stack.push(30)

# Display the stack
stack.display()  # Output: Stack: [10, 20, 30]

# Peek at the top item
print("Top item:", stack.peek())  # Output: Top item: 30

# Pop an item
print("Popped item:", stack.pop())  # Output: Popped item: 30

# Display the stack after popping
stack.display()  # Output: Stack: [10, 20]

# Check if the stack is empty
print("Is stack empty?", stack.is_empty())  # Output: False

# Get the size of the stack
print("Stack size:", stack.size())  # Output: Stack size: 2
