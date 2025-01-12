
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
        # Edgecase: what if dict is empty. well in that case point head and tail to new node
        if self.head is None:
            self.head = new_node
        # link last Node of LL to new node
        else:self.tail.next = new_node
        # and then tail (copy last link pointer)
        self.tail = new_node
        self.length += 1
        return True


    def make_empty(self):
        '''To check Edge case of append use this.'''
        self.head = None
        self.tail = None
        self.length = 0






ll = LinkedList(5)
ll.append(7)
ll.append(9)
print (ll.head.value,ll.head.next.value,ll.head.next.next.value, ll.tail.value)




