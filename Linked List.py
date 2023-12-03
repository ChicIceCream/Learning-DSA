class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None
        
class linked_list:
    def __init__(self):
        self.head = None 

    def insert_at_begining(self, data):
        node = Node(data), self.head
        self.head = node 
        
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        while itr:
            itr = itr.next
        

if __name__ == '__main__':
    pass
        