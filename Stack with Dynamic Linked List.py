class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Pointer to the next node in the stack

class Stack:
    def __init__(self):
        self.top = None  # The top of the stack (head of the linked list)
        self.size = 0  # Keep track of the stack size

    def is_empty(self):
        """Check if the stack is empty."""
        return self.top is None

    def push(self, data):
        """Push an item onto the stack."""
        new_node = Node(data)  # Create a new node
        new_node.next = self.top  # Set the next of the new node to the current top
        self.top = new_node  # Make the new node the top of the stack
        self.size += 1  # Increment size of the stack

    def pop(self):
        """Pop an item from the stack."""
        if self.is_empty():
            return "Stack is empty!"  # Return message if stack is empty
        popped_node = self.top  # Get the current top node
        self.top = self.top.next  # Set the next node as the new top
        popped_node.next = None  # Disconnect the popped node from the stack
        self.size -= 1  # Decrement size of the stack
        return popped_node.data  # Return the data of the popped node

    def peek(self):
        """Peek at the top item of the stack."""
        if self.is_empty():
            return "Stack is empty!"  # Return message if stack is empty
        return self.top.data  # Return the data of the top node

    def get_size(self):
        """Return the size of the stack."""
        return self.size

    def display(self):
        """Display all items in the stack."""
        if self.is_empty():
            print("Stack is empty.")
            return
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # To show the end of the stack

# Example usage:
stack = Stack()

# Push items onto the stack
stack.push(10)
stack.push(20)
stack.push(30)

# Display the stack
stack.display()  # Output: 30 -> 20 -> 10 -> None

# Peek at the top item
print("Top item:", stack.peek())  # Output: Top item: 30

# Pop an item
print("Popped item:", stack.pop())  # Output: Popped item: 30

# Display the stack after popping
stack.display()  # Output: 20 -> 10 -> None

# Check if the stack is empty
print("Is stack empty?", stack.is_empty())  # Output: False

# Get the size of the stack
print("Stack size:", stack.get_size())  # Output: Stack size: 2
