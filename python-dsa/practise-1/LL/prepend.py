
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

    def print_list(self):
        print("printing list")
        temp  = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0



ll = LinkedList(3)
ll.prepend(2)
ll.print_list()
ll.make_empty()
ll.print_list()
ll.prepend(1)
ll.print_list()
