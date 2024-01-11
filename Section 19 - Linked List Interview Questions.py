from random import randint


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None

    def __iter__(self):
        curr_node = self.head
        while curr_node:
            yield curr_node
            curr_node = curr_node.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return ' -> '.join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def add(self, value):
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self

# customLL = LinkedList()
# customLL.generate(10, 0, 99)
# print(customLL)
# print(len(customLL))

# TODO: ask dad for below function
def remove_duplicates(ll):
    if ll.head is None:
        return

    current_node = ll.head
    prev_node = None

    while current_node:
        runner = current_node
        while runner.next:
            if runner.next.value == current_node.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        prev_node = current_node
        current_node = current_node.next

    ll.tail = prev_node
    return ll.head

#TODO: ask dad for the logic behind it

def nth_to_last(ll, n):
    pointer1 = ll.head
    pointer2 = ll.head

    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next

    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1


def partition(ll, x):
    curr_node = ll.head
    ll.tail = ll.head

    while curr_node:
        next_node = curr_node.next
        curr_node.next = None
        if curr_node.value < x:
            curr_node.next = ll.head
            ll.head = curr_node
        else:
            ll.tail.next = curr_node
            ll.tail = curr_node
        curr_node = next_node
    if ll.tail.next is not None:
        ll.tail.next = None


def sum_list(llA, llB):
    n1 = llA.head
    n2 = llB.head
    carry = 0
    ll = LinkedList()

    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        ll.add(int(result % 10))
        carry = result / 10
    return ll


def intersection(llA, llB): #O(A+B) Time complexity, O(1) space complexity
    if llA.tail is not llB.tail:
        return False

    lenA = len(llA)
    lenB = len(llB)

    shorter = llA if lenA < lenB else llB
    longer = llB if lenA < lenB else llA

    diff = len(longer) - len(shorter)

    longer_node = longer.head
    shorter_node = shorter.head

    for i in range(diff):
        longer_node = longer_node.next
    while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next

    return longer_node


def add_same_node(llA, llB, value):
    temp_node = Node(value)

    llA.tail.next = temp_node
    llA.tail = temp_node

    llB.tail.next = temp_node
    llB.tail = temp_node
