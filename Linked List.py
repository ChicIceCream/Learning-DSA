# class Node:
    
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# # Start creating nodes
# # 1st node
# Node = Node(10)
# # 2nd node
# node2 = Node(20)
# # 3rd node
# node3 = Node(30)
# # 4th node
# node4 = Node(40)

# # Assign the next node to each node
# Node.next = node2
# node2.next = node3
# node3.next = node4

# # Printing the linked list
# current = Node
# while current is not None:
#     print(f'{current.data}', end='->')
#     current = current.next
# print(f'None')

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node

    # def prepend(self, data):
    #     new_node = Node(data)
    #     new_node.next = self.head
    #     self.head = new_node

    # def delete_with_value(self, data):
    #     if self.head is None:
    #         return
    #     if self.head.data == data:
    #         self.head = self.head.next
    #         return
    #     current_node = self.head
    #     while current_node.next:
    #         if current_node.next.data == data:
    #             current_node.next = current_node.next.next
    #             return
    #         current_node = current_node.next

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(f'{current_node.data}', end=' --> ')
            current_node = current_node.next
        print('None')

# Example usage:

linked_list = LinkedList()

# Append nodes
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)

# Print list
linked_list.print_list()

# Prepend node
# linked_list.prepend(5)

# Print list again
linked_list.print_list()

# Delete a node with value 20
# linked_list.delete_with_value(20)

# Print list again
linked_list.print_list()
