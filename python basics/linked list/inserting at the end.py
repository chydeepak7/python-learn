class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self,data):
        if self.head is None:
            node = Node(data)
            self.head = node
            return
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data)
            return

    def print(self):
        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next

ll1 = LinkedList()
ll1.insert_at_end(3)
ll1.insert_at_end(36)
ll1.print()




