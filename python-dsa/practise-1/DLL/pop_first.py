class Node:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head  = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

## DLL: Append
print("------------------------------------------------------------------------------")

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)

print('Head:', my_doubly_linked_list.head.value)
print('Tail:', my_doubly_linked_list.tail.value)
print('Length:', my_doubly_linked_list.length, '\n')

print('Doubly Linked List:')
my_doubly_linked_list.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    Head: 1
    Tail: 2
    Length: 2 

    Doubly Linked List:
    1
    2

"""

print("------------------------------------------------------------------------------")
## DLL: Pop
print("------------------------------------------------------------------------------")

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)


# (2) Items - Returns 2 Node
print(my_doubly_linked_list.pop().value)
# (1) Item -  Returns 1 Node
print(my_doubly_linked_list.pop().value)
# (0) Items - Returns None
print(my_doubly_linked_list.pop())



"""
    EXPECTED OUTPUT:
    ----------------
    2
    1
    None

"""
print("------------------------------------------------------------------------------")
## DLL: Prepend
print("------------------------------------------------------------------------------")
my_doubly_linked_list = DoublyLinkedList(2)
my_doubly_linked_list.append(3)
print('Before prepend():')
print('----------------')
print('Head:', my_doubly_linked_list.head.value)
print('Tail:', my_doubly_linked_list.tail.value)
print('Length:', my_doubly_linked_list.length, '\n')
print('Doubly Linked List:')
my_doubly_linked_list.print_list()

my_doubly_linked_list.prepend(1)

print('\n\nAfter prepend():')
print('---------------')
print('Head:', my_doubly_linked_list.head.value)
print('Tail:', my_doubly_linked_list.tail.value)
print('Length:', my_doubly_linked_list.length, '\n')
print('Doubly Linked List:')
my_doubly_linked_list.print_list()

"""
    EXPECTED OUTPUT:

    Before prepend():
    ----------------
    Head: 2
    Tail: 3
    Length: 2 

    Doubly Linked List:
    2
    3


    After prepend():
    ---------------
    Head: 1
    Tail: 3
    Length: 3 

    Doubly Linked List:
    1
    2
    3

"""
print("------------------------------------------------------------------------------")
## DLL: Pop First
print("------------------------------------------------------------------------------")

my_doubly_linked_list = DoublyLinkedList(2)
my_doubly_linked_list.append(1)


# (2) Items - Returns 2 Node
print(my_doubly_linked_list.pop_first().value)
# (1) Item -  Returns 1 Node
print(my_doubly_linked_list.pop_first().value)
# (0) Items - Returns None
print(my_doubly_linked_list.pop_first())



"""
    EXPECTED OUTPUT:
    ----------------
    2
    1
    None

"""
print("------------------------------------------------------------------------------")