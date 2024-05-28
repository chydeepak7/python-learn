class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insertatbeg(self,data):
        node = Node(data,self.head)
        self.head = node

    def print(self):
        itr = self.head
        while itr:
            print(str(itr.data))
            itr = itr.next


ll1 = LinkedList()
ll1.insertatbeg(5)
ll1.insertatbeg(5)
ll1.insertatbeg(54)
ll1.print()
