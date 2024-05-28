class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data)


    def print(self):
        lstr = ''
        temp = self.head
        while temp:
            lstr += str(temp.data) + ' -> '
            temp = temp.next
        print(lstr)


ll = LinkedList()
ll.insert_at_begining(1)
ll.insert_at_begining(2)
ll.insert_at_end(2)
ll.insert_at_begining(9)
ll.print()
