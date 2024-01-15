#Three in one

class MultiStack:
    def __init__(self, stack_size):
        self.number_stacks = 3
        self.custom_list = [0] * (stack_size * self.number_stacks)
        self.sizes = [0] * self.number_stacks
        self.stack_size = stack_size

    def is_full(self, stack_num):
        if self.sizes[stack_num] == self.stack_size:
            return True
        else:
            return False

    def is_empty(self, stack_num):
        if self.sizes[stack_num] == 0:
            return True
        else:
            return False

    def index_of_top(self, stack_num):
        offset = stack_num * self.stack_size
        return offset + self.sizes[stack_num] - 1

    def push(self, item, stack_num):
        if self.is_full(stack_num):
            return 'The stack is full'
        else:
            self.sizes[stack_num] += 1
            self.custom_list[self.index_of_top(stack_num)] = item

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            return 'The stack is empty'
        else:
            value = self.custom_list[self.index_of_top(stack_num)]
            self.custom_list[self.index_of_top(stack_num)] = 0
            self.sizes[stack_num] -= 1
            return value

    def peek(self, stack_num):
        if self.is_empty(stack_num):
            return 'The stack is empty'
        else:
            value = self.custom_list[self.index_of_top(stack_num)]
            return value


# Stack minimum
class Node:
    def __init__(self, value=Next, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        string = str(self.value)
        if self.next:
            str += ',' + str(self.next)
        return string


class Stack:
    def __init__(self):
        self.top = None
        self.min_node = None

    def min(self):
        if not self.min_node:
            return None
        return self.min_node.value

    def push(self, item):
        if self.min_node and (self.min_node.value < item):
            self.min_node = Node(value=self.min_node.value, next=self.min_node)
        else:
            self.min_node = Node(value=item, next=self.min_node)
        self.top = Node(value=item, next=self.top)

    def pop(self):
        if not self.top:
            return None
        self.min_node = self.min_node.next
        item = self.top.value
        self.top = self.top.next
        return item


#Stack of Plates
class PlateStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def __str__(self):
        return self.stacks

    def push(self, item):
        if len(self.stacks) > 0 and (len(self.stacks[-1])) < self.capacity:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])

    def pop(self):
        while len(self.stacks) and len(self.stacks[-1] == 0):
            self.stacks.pop()
        if len(self.stacks) == 0:
            return None
        else:
            return self.stacks[-1].pop()

    def pop_at(self, stack_number):
        if len(self.stacks[stack_number] > 0):
            return self.stacks[stack_number].pop()
        else:
            return None


#Queue via Stacks

class StackForQueue:
    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)

    def push(self, item):
        self.list.append(item)

    def pop(self):
        if len(self.list) == 0:
            return  None
        return self.list.pop()


class QueueViaStack:
    def __init__(self):
        self.in_stack = StackForQueue()
        self.out_stack = StackForQueue()

    def enqueue(self, item):
        self.in_stack.push(item)

    def dequeue(self):
        while len(self.in_stack):
            self.out_stack.push(self.in_stack.pop())
        result = self.out_stack.pop()
        while len(self.out_stack):
            self.in_stack.push(self.out_stack.pop())
        return result


#Animal Shelter
class AnimalShelter:
    def __init__(self):
        self.cats = []
        self.dogs = []

    def enqueue(self, animal, type):
        if type == 'Cat':
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeue_cat(self):
        if len(self.cats) == 0:
            return None
        else:
            cat = self.cats.pop(0)
            return cat

    def dequeue_dog(self):
        if len(self.dogs) == 0:
            return None
        else:
            dog = self.dogs.pop(0)
            return dog
        
    def dequeue_any(self):
        if len(self.cats) == 0:
            result = self.dogs.pop(0)
        else:
            result = self.cats.pop(0)
        return result
