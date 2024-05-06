class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def insert(self, new_node):
    if self.head is None:
      self.head = new_node
      return
    last_node = self.head
    while last_node.next:
      last_node = last_node.next
    last_node.next = new_node

  def print_list(self):
    current_node = self.head
    while current_node:
      print(current_node.data)
      current_node = current_node.next

# Create a Singly Linked List
linked_list = LinkedList()

# Insert nodes into the linked list
linked_list.insert(Node("John"))
linked_list.insert(Node("Ben"))
linked_list.insert(Node("Matthew"))

# Print the linked list
linked_list.print_list()
