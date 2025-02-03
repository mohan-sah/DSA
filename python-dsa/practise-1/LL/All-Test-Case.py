## Append
print("------------------------------------------------------------------------------")

my_linked_list = LinkedList(1)
my_linked_list.make_empty()

my_linked_list.append(1)
my_linked_list.append(2)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')

print('Linked List:')
my_linked_list.print_list()
print("------------------------------------------------------------------------------")
"""
    EXPECTED OUTPUT:
    ----------------
    Head: 1
    Tail: 2
    Length: 2

    Linked List:
    1
    2

"""

##LL: Pop
print("------------------------------------------------------------------------------")
my_linked_list = LinkedList(1)
my_linked_list.make_empty()

my_linked_list.append(1)
my_linked_list.append(2)
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')

print('Linked List:')
my_linked_list.print_list()
print(' pop:', my_linked_list.pop().value)
print(' pop:', my_linked_list.pop().value)

"""
    EXPECTED OUTPUT:
    ----------------
    Head: 1
    Tail: 2
    Length: 2 

    Linked List:
    1
    2
     pop: 2
     pop: 1

"""

print("------------------------------------------------------------------------------")
##LL: Prepend

print("------------------------------------------------------------------------------")
my_linked_list = LinkedList(2)
my_linked_list.append(3)

print('Before prepend():')
print('----------------')
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')
print('Linked List:')
my_linked_list.print_list()

my_linked_list.prepend(1)

print('\n\nAfter prepend():')
print('---------------')
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')
print('Linked List:')
my_linked_list.print_list()
print("------------------------------------------------------------------------------")
"""
    EXPECTED OUTPUT:

    Before prepend():
    ----------------
    Head: 2
    Tail: 3
    Length: 2

    Linked List:
    2
    3


    After prepend():
    ---------------
    Head: 1
    Tail: 3
    Length: 3

    Linked List:
    1
    2
    3

"""

##LL: Pop First

print("------------------------------------------------------------------------------")
my_linked_list.make_empty()
my_linked_list = LinkedList(2)
my_linked_list.append(1)

# (2) Items - Returns 2 Node
print(my_linked_list.pop_first().value)
# (1) Item -  Returns 1 Node
print(my_linked_list.pop_first().value)
# (0) Items - Returns None
print(my_linked_list.pop_first())

print("------------------------------------------------------------------------------")

"""
    EXPECTED OUTPUT:
    ----------------
    2
    1
    None

"""
##LL: Get
print("------------------------------------------------------------------------------")

my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

print("get() value 3 :", my_linked_list.get(3).value)
print("------------------------------------------------------------------------------")

"""
    EXPECTED OUTPUT:
    ----------------
    get() value 3 : 3

"""

##LL: Set
print("------------------------------------------------------------------------------")
my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

print('LL before set_value():')
my_linked_list.print_list()

my_linked_list.set_value(1, 4)

print('\nLL after set_value():')
my_linked_list.print_list()
print("------------------------------------------------------------------------------")

"""
    EXPECTED OUTPUT:
    ----------------
    LL before set_value():
    11
    3
    23
    7

    LL after set_value():
    11
    4
    23
    7
"""

## LL: Insert


print("------------------------------------------------------------------------------")
my_linked_list = LinkedList(1)
my_linked_list.append(3)

print('LL before insert():')
my_linked_list.print_list()

my_linked_list.insert(1, 2)

print('\nLL after insert(2) in middle:')
my_linked_list.print_list()

my_linked_list.insert(0, 0)

print('\nLL after insert(0) at beginning:')
my_linked_list.print_list()

my_linked_list.insert(4, 4)

print('\nLL after insert(4) at end:')
my_linked_list.print_list()
print("------------------------------------------------------------------------------")

"""
    EXPECTED OUTPUT:
    ----------------
    LL before insert():
    1
    3

    LL after insert(2) in middle:
    1
    2
    3

    LL after insert(0) at beginning:
    0
    1
    2
    3

    LL after insert(4) at end:
    0
    1
    2
    3
    4

"""

## LL: Remove


print("------------------------------------------------------------------------------")
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print('LL before remove():')
my_linked_list.print_list()

print('\nRemoved node:')
print(my_linked_list.remove(2).value)
print('LL after remove() in middle:')
my_linked_list.print_list()

print('\nRemoved node:')
print(my_linked_list.remove(0).value)
print('LL after remove() of first node:')
my_linked_list.print_list()

print('\nRemoved node:')
print(my_linked_list.remove(2).value)
print('LL after remove() of last node:')
my_linked_list.print_list()
print("------------------------------------------------------------------------------")

"""
    EXPECTED OUTPUT:
    ----------------
    LL before remove():
    1
    2
    3
    4
    5

    Removed node:
    3
    LL after remove() in middle:
    1
    2
    4
    5

    Removed node:
    1
    LL after remove() of first node:
    2
    4
    5

    Removed node:
    5
    LL after remove() of last node:
    2
    4

"""

## LL : Reverse

print("------------------------------------------------------------------------------")
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

print('LL before reverse():')
my_linked_list.print_list()

my_linked_list.reverse()

print('\nLL after reverse():')
my_linked_list.print_list()
print("------------------------------------------------------------------------------")
"""
    EXPECTED OUTPUT:
    ----------------
    LL before reverse():
    1
    2
    3
    4

    LL after reverse():
    4
    3
    2
    1

"""
