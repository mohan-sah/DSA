


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

    def print_list(self):
        print("Printing List")
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        print("Printing List end")

    def append(self,calue):
        new_node = Node(calue)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.length  += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        prev = self.head
        while temp.next is not None:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp





my_linked_list = LinkedList(5)
my_linked_list.append(7)
my_linked_list.append(9)
my_linked_list.print_list()
my_linked_list.pop()
my_linked_list.print_list()
print(my_linked_list.pop())
print(my_linked_list.pop())
print(my_linked_list.pop())
print(my_linked_list.pop())

