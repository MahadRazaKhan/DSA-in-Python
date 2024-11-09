class Node:
    def __init__(self, data):
        self.data = data  # The data of the node
        self.next = None  # Pointer to the next node in the queue

class Queue:
    def __init__(self):
        self.front = None  # Pointer to the front of the queue
        self.rear = None   # Pointer to the rear of the queue
        self.size = 0      # Size of the queue

    def is_empty(self):
        """Check if the queue is empty."""
        return self.front is None

    def enqueue(self, data):
        """Add an item to the rear of the queue."""
        new_node = Node(data)  # Create a new node
        if self.is_empty():
            self.front = self.rear = new_node  # Both front and rear point to the new node
        else:
            self.rear.next = new_node  # Link the current rear node to the new node
            self.rear = new_node  # Update the rear to point to the new node
        self.size += 1  # Increment size of the queue

    def dequeue(self):
        """Remove an item from the front of the queue."""
        if self.is_empty():
            return "Queue is empty!"  # Return a message if the queue is empty
        dequeued_node = self.front  # Get the front node
        self.front = self.front.next  # Move the front pointer to the next node
        if self.front is None:  # If the queue becomes empty after the dequeue
            self.rear = None  # Set rear to None as well
        dequeued_node.next = None  # Disconnect the dequeued node
        self.size -= 1  # Decrement the size of the queue
        return dequeued_node.data  # Return the data of the dequeued node

    def peek(self):
        """View the front item of the queue without removing it."""
        if self.is_empty():
            return "Queue is empty!"
        return self.front.data  # Return the data of the front node

    def get_size(self):
        """Return the size of the queue."""
        return self.size

    def display(self):
        """Display all the items in the queue."""
        if self.is_empty():
            print("Queue is empty.")
            return
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # To indicate the end of the queue

# Example usage:
queue = Queue()

# Enqueue items
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

# Display the queue
queue.display()  # Output: 10 -> 20 -> 30 -> None

# Peek at the front item
print("Front item:", queue.peek())  # Output: Front item: 10

# Dequeue an item
print("Dequeued item:", queue.dequeue())  # Output: Dequeued item: 10

# Display the queue after dequeuing
queue.display()  # Output: 20 -> 30 -> None

# Check if the queue is empty
print("Is queue empty?", queue.is_empty())  # Output: False

# Get the size of the queue
print("Queue size:", queue.get_size())  # Output: Queue size: 2
