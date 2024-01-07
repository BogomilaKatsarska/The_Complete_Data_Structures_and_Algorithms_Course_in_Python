'''
- Each node has two references and the first and last node refer to each other
'''

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next: #in order to avoid infinite loop
                break

    def create(self, node_value):
        new_node = Node(node_value)
        self.head = new_node
        self.tail = new_node
        new_node.prev = new_node
        new_node.next = new_node
        return 'The CDLL is created successfully.'

    def insert(self, value, location):
        if self.head is None:
            return "The CDLL does not exist"
        else:
            new_node = Node(value)
            if location == 0:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.head = new_node
                self.tail.next = new_node
            elif location == 1:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                new_node.next = temp_node.next
                new_node.prev = temp_node
                new_node.next.prev = new_node
                temp_node.next = new_node
            return 'The node has been successfully inserted'

    def traverse(self):
        if self.head is None:
            return "The CDLL does not exist"
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                if temp_node == self.tail:
                    break
                temp_node = temp_node.next

    def reverse_traverse(self):
        if self.head is None:
            return "The CDLL does not exist"
        else:
            temp_node = self.tail
            while temp_node:
                print(temp_node.value)
                if temp_node == self.head:
                    break
                temp_node = temp_node.prev

    def search(self, node_value):
        if self.head is None:
            return "There is not any node in CDLL"
        else:
            temp_node = self.head
            while temp_node:
                if temp_node.value == node_value:
                    return temp_node.value
                if temp_node == self.tail:
                    return "The value does not exist in CDLL"
                temp_node = temp_node.next

    def delete_node(self, location):
        if self.head is None:
            print("There is not any node to delete")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                current_node = self.head
                index = 0
                while index < location -1:
                    current_node = current_node.next
                    index += 1
                current_node.next = current_node.next.next
                current_node.next.prev = current_node
            print("The node has been successfully delete")

    def delete_cdll(self):
        if self.head is None:
            print('There is not any element to delete.')
        else:
            self.tail.next = None
            temp_node = self.head
            while temp_node:
                temp_node.prev = None
                temp_node = temp_node.next
            self.head = None
            self.tail = None
            print('The CDLL has been successfully deleted.')

