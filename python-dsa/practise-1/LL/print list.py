


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

        #ok, this is inside of dict what's next
class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length =   1

    def print_list(self,value):
        temp = Node(value)
        while temp is not None:
            print(temp.value)
            temp = temp.next

my_linked_list = LinkedList(5)

