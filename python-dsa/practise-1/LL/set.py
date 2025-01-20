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

    # Append and pop (operation done at last)
    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        temp = self.head
        prev = None
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        while temp.next is not None:
            prev = temp
            temp =  temp.next
        self.tail.next = None
        self.tail = prev
        self.length -= 1
        return temp

    # extra function, printing and get indexed node
    def print_list(self):
        temp = self.head
        image = ''
        while temp is not None:
            image += f"{str(temp.value)}--> "
            temp = temp.next
        print(image)
    def get(self,index):
        if index < 0 or index > self.length:
            return  None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    # add and remove at first

    def prepend(self,value):
        temp = Node(value)
        if self.length == 0:
            self.head = temp
            self.tail = temp
        temp.next = self.head
        self.head = temp
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    #  editing value in middle
    def set_value(self,index,value):
        if index > self.length or index<0:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        current.value = value
        return True



# Test cases
my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

print('LL before set_value():')
my_linked_list.print_list()

my_linked_list.set_value(1,4)

print('\nLL after set_value():')
my_linked_list.print_list()