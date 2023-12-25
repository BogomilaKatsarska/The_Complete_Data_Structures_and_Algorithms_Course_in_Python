'''
1.Lined List:
    - a form of sequential collection and it does not have to be in order
    - made up of independent nodes that may contain any type of data
    - each node has a reference to the next node in the list
    - nodes: data and link to the next node
    |HEAD| 001 - ref to 1st node |-->|1|111 - ref to 2nd node| -> |2| 222 - ref to the 3rd node ..... |5|Null (TAIL)

2. Arrays vs Linked Lists:
    2.1. Array:
        - we have indexes
        - elements are contiguous with each other
    2.2. Linked List
        - we do not have indexes
        - elements are not contiguous, not located next to each other
        - last node points to NONE

3. Types of Linked Lists:
    3.1. Singly Linked List:
        - each node has a reference to the next one and no reference to the previous one
    3.2. Circular Singly Linked List
        - the last node of the list has a node to the first element(ex: chess game)
    3.3. Doubly Linked List
        - we have 2 references for each node - to the previous and to the following node
        - flexibility of traversing in both directions(ex: music playlist on phone)
    3.4. Circular Doubly Linked List
        - we have 2 reference for each node + the last and the first node also have references to each other

4. Linked List in memory:
    - not contiguously i.e. randomly

5. Node Class Constructor:
{
    'value': 10,
    'next': None
}
    - To create empty linked list:

    class LinkedList:
        def __init__(self):
            self.head = None
            self.tail = None
'''

'''
class LinkedListDemo:
    def __init__(self, value): #O(1)
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


new_linked_list = LinkedListDemo(10)
print(new_linked_list.head)
print(new_linked_list.head.value)
print(new_linked_list.tail.value)
print(new_linked_list.length)
'''
##################################


class LikedListEmpty:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


##################################
class Node:

    def __init__(self, value):      #Time complexity: O(1), Space complexity: O(1)
        self.value = value
        self.next = None            #when we create initially a new node we do not know its neighbour


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

    def append(self, value): #O(1)
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    #prepend() at the beginning of the list
    def prepend(self, value):        #O(1)
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        elif self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):             #O(n)
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True

    def traverse(self):
        current_node = self.head
        while current_node is not None: #can use 'while current_node:'        #O(n)
            print(current_node.value)
            current_node = current_node.next

    def search(self, target):
        current = self.head
        index = 0
        while current is not None:
            if current.value == target:
                return index
            current = current.next
            index += 1
        return "The target value does not exist"

    def get(self, index):
        if index == -1:
            return self.tail
        if index < -1 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):                 #O(n)
            current = current.next
        return current

    def set_value(self, index, value):
        temp = self.get(index)                 #O(n)
        if temp:
            temp.value = value
            return True
        return False

    def pop_first(self):                       #O(1)
        if self.length == 0:
            return None

        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
            self.length -= 1
        return popped_node

    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:            #O(n)
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -= 1
        return popped_node

    def remove(self, index):
        if index >= self.length or index < -1:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1 or index == -1:
            return self.pop()                            #O(n)
        prev_node = self.get(index-1)                    #O(n)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1

        return popped_node

    def delete_all(self):
        self.head = None                                   #O(1)
        self.tail = None
        self.length = 0


new_ll = LinkedList()
new_ll.append(1)
new_ll.append(2)
new_ll.append(3)
print(new_ll)
new_ll.prepend(0)
print(new_ll)
new_ll.insert(2, 50)
print(new_ll)