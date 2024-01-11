'''
1.Stack:
    - data structure that stores items in a LIFO manner
    - example: back btn in the browser
    - creating stack by using list: speed problems when it grows, easy to implement

2. Use and Avoid:
    2.1. Use:
        - when we want LIFO functionality
        - cannot be easily corrupted(can only insert in the end of the stack)
    2.2. Avoid:
        - random access is not possible
'''
#create
custom_stack = []
#push - adds element on top of each other i.e. as last
custom_stack.push()
#pop - returns and deletes last el
custom_stack.pop()
#peek - returns the last element without removing it from the stack
custom_stack.peek()
#isEmpty
custom_stack.isEmpty()
#isFull
custom_stack.isFull()
#delete
custom_stack.delete()


class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def push(self, value):
        self.list.append(value)
        return 'The element has been successfully inserted.'

    def pop(self):
        if self.isEmpty():
            return 'There is not any element in the stack'
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return 'There is not any element in the stack'
        else:
            return self.list[len(self.list) - 1]

    def delete(self):
        self.list = None

'''
Stack with Limited Size
'''

class StackLimitSize:
    def __init__(self, max_size):
        self.max_size = max_size
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return 'n'.join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def isFull(self):
        if len(self.list) == self.max_size:
            return True
        else:
            return False

    def push(self, value):
        if self.isFull():
            return 'The stack is full'
        else:
            self.list.append(value)
            return 'The element has been successfully inserted'

    def pop(self):
        if self.isEmpty():
            return 'There is not any element in the stack'
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return 'There is not any element in the stack'
        else:
            return self.list[len(self.list) - 1]

    def delete(self):
        self.list = None


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None


class StackLL:
    def __init__(self):
        self.LinkedList = LinkedList()

    def is_empty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        if self.is_empty():
            return "There is not any element in the stack"
        else:
            node_value = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return node_value

    def peek(self):
        if self.is_empty():
            return "There is not any element in the stack"
        else:
            node_value = self.LinkedList.head.value
            return node_value

    def delete(self):
        self.LinkedList.head = None
