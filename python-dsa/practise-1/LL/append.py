
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self,value):
        new_node = Node(value)
        # link last Node of LL to new node
        self.tail.next = new_node
        self.tail = new_node


ll = LinkedList(5)
ll.append(7)
ll.append(9)
print (ll.head.value,ll.head.next.value,ll.head.next.next.value, ll.tail.value)



