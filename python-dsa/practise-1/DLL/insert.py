
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
        self.length +=1
        return True

    def pop(self):
        if self.length == 0:
            return  None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail= self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return  temp

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

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
        return  True

    def pop_first(self):
        if self.length == 0:
            return  None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head= self.head.next
            temp.next = None
            self.head.prev = None
        self.length -= 1
        return  temp

    def get(self,index):
        if 0>index>self.length:
            return  None
        temp = self.head
        if index< self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1,index,-1):
                temp = temp.prev
        return temp

    def set_value(self,index,value):
        if 0>index>self.length:
            return  None
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        else:
            return False

    def insert(self,index,value):
        if 0>index>self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return  self.append(value)
        new_node = Node(value)
        before = self.get(index -1)
        after = before.next
        before.next = new_node
        new_node.prev = before
        new_node.next = after
        after.prev = new_node
        self.length += 1
        return True




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
## DLL: Get
print("------------------------------------------------------------------------------")

my_doubly_linked_list = DoublyLinkedList(0)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)

print('Get node from first half of DLL:')
print(my_doubly_linked_list.get(1).value)

print('\nGet node from second half of DLL:')
print(my_doubly_linked_list.get(2).value)



"""
    EXPECTED OUTPUT:
    ----------------
    Get node from first half of DLL:
    1

    Get node from second half of DLL:
    2

"""
print("------------------------------------------------------------------------------")
## DLL: Set
print("------------------------------------------------------------------------------")

my_doubly_linked_list = DoublyLinkedList(11)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(23)
my_doubly_linked_list.append(7)

print('DLL before set_value():')
my_doubly_linked_list.print_list()

my_doubly_linked_list.set_value(1,4)

print('\nDLL after set_value():')
my_doubly_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    DLL before set_value():
    11
    3
    23
    7

    DLL after set_value():
    11
    4
    23
    7

"""
print("------------------------------------------------------------------------------")
## DLL: Insert
print("------------------------------------------------------------------------------")

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(3)


print('DLL before insert():')
my_doubly_linked_list.print_list()


my_doubly_linked_list.insert(1,2)

print('\nDLL after insert(2) in middle:')
my_doubly_linked_list.print_list()


my_doubly_linked_list.insert(0,0)

print('\nDLL after insert(0) at beginning:')
my_doubly_linked_list.print_list()


my_doubly_linked_list.insert(4,4)

print('\nDLL after insert(4) at end:')
my_doubly_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    DLL before insert():
    1
    3

    DLL after insert(2) in middle:
    1
    2
    3

    DLL after insert(0) at beginning:
    0
    1
    2
    3

    DLL after insert(4) at end:
    0
    1
    2
    3
    4

"""
print("------------------------------------------------------------------------------")




