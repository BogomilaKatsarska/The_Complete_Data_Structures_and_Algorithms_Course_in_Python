'''
1.Queue:
    - stores items in FIFO manner
    - utilize first coming data first, while others wait for their turn
    - example: sale system of a restaurant, call center phone systems

2.Circular Queue: Queue with fixed capacity

3.Queue Modules:
    - Collections Module:
        - The collections.deque Class
            deque()
            append()
            popleft()
            clear()
    - Queue Module
    - Multiprocessing Module
'''

custom_queue = []
# enqueue() == insert
custom_queue.enqueue(1)
# dequeue() == pop
#peek() - not removing the element, but returning it
#isEmpty()
#isFull()
#delete()


class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def is_empty(self):
        if self.items == []:
            return True
        else:
            return False

    def enqueue(self, value):
        self.items.append(value)
        return 'The element is inserted at the end of the queue'

    def dequeue(self):
        if self.is_empty():
            return 'There is not any element in the queue'
        else:
            return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return 'There is not any element in the queue'
        else:
            return self.items[0]

    def delete(self):
        self.items = None


class CircularQueue:
    def __init__(self, max_size):
        self.items = max_size * [None]
        self.max_size = max_size
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def is_full(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.max_size:
            return True
        else:
            return False

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def enqueue(self, value):
        if self.is_full():
            return 'The queue is full'
        if self.top + 1 == self.max_size:
            self.top = 0
        else:
            self.top += 1
            if self.start == -1:
                self.start = 0
            self.items[self.top] = value
            return 'The element is inserted at the end of the queue'

    def dequeue(self):
        if self.is_empty():
            return 'There is not any element in the queue'
        else:
            first_element = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.max_size:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return first_element

    def peek(self):
        if self.is_empty():
            return 'There is not any element in the queue'
        else:
            return self.items[self.start]

    def delete(self):
        self.items = self.max_size * [None]
        self.top = -1
        self.start = -1


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curr_node = self.head
        while curr_node:
            yield curr_node
            curr_node = curr_node.next


class QueueWithLinkedList:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)

    def enqueue(self, value):
        new_node = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = new_node
            self.linkedList.tail = new_node
        else:
            self.linkedList.tail.next = new_node
            self.linkedList.tail = new_node

    def is_empty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False

    def dequeue(self):
        if self.is_empty():
            return 'There is not any node in the queue'
        else:
            temp_node = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return temp_node

    def peek(self):
        if self.is_empty():
            return 'There is not any node in the queue'
        else:
            return self.linkedList.head

    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None

''''
Collections Module
'''

from collections import deque

custom_queue_2 = deque(maxlen=3)
custom_queue_2.append(1)
custom_queue_2.append(2)
custom_queue_2.append(3)
custom_queue_2.popleft()
custom_queue_2.clear()

'''
Queue Module
'''
import queue as q

custom_queue_3 = q.Queue(maxsize=3)
print(custom_queue_3.qsize()) #returns the size of the queue
custom_queue_3.put(3) #put inserts element at the end of the queue
print(custom_queue_3.empty()) #boolean
print(custom_queue_3.full())#if the max size is reached
print(custom_queue_3.get()) #returns first el of the queue

'''
Multiprocessing Module
'''
from multiprocessing import Queue
custom_queue_4 = Queue(maxsize=3)
custom_queue_4.put(1)
print(custom_queue_4.get())