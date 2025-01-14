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
        if self.length == 0:
            self.tail = new_node
            self.head = new_node
        self.tail.next = new_node
        self.tail = self.tail.next

        self.length +=1
        return True

    def print_list(self):
        print('printing started..')
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def get(self,index:int):
        temp = self.head
        temp_index = 0
        while temp_index != index:
            temp_index += 1
            temp = temp.next
        return temp.value



ll = LinkedList(3)
ll.append(4)
ll.append(5)
ll.print_list()
print("getting value of given index is :" +str(ll.get(2)))
