class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Initialize next pointer to None

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the linked list with no nodes

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            # If the list is empty, make the new node the head
            self.head = new_node
        else:
            # Traverse to the end of the list and append the new node
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            # Insert at the beginning (make it the head)
            new_node.next = self.head
            self.head = new_node
        else:
            # Insert at the given position
            current = self.head
            count = 0
            while current and count < position - 1:
                current = current.next
                count += 1
            if current is None:
                print("Position out of bounds.")
            else:
                new_node.next = current.next
                current.next = new_node

    def display_all(self):
        if not self.head:
            print("The list is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # To indicate the end of the list

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                print(f"Element {key} found in the list.")
                return
            current = current.next
        print(f"Element {key} not found in the list.")

    def delete(self, key):
        current = self.head
        if current is None:
            print("The list is empty.")
            return
        if current.data == key:
            # If the element to delete is the head
            self.head = current.next
            current = None
            print(f"Element {key} deleted from the list.")
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            print(f"Element {key} not found in the list.")
            return
        prev.next = current.next
        current = None
        print(f"Element {key} deleted from the list.")

# Example Usage
linked_list = LinkedList()

# Append items
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

# Display all
print("Linked List:")
linked_list.display_all()

# Insert item
linked_list.insert(25, 2)  # Insert 25 at position 2

# Display after insert
print("Linked List after insertion:")
linked_list.display_all()

# Search for an element
linked_list.search(20)
linked_list.search(40)

# Delete an element
linked_list.delete(20)

# Display after deletion
print("Linked List after deletion:")
linked_list.display_all()
