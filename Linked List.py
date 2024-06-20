class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
# Start creating nodes
# 1st node
node1 = Node(10)
# 2nd node
node2 = Node(20)
# 3rd node
node3 = Node(30)
# 4th node
node4 = Node(40)

# Assign the next node to each node
node1.next = node2
node2.next = node3
node3.next = node4

# Printing the linked list
current = node1
while current is not None:
    print(f'{current.data}', end='->')
    current = current.next
print(f'None')