'''
1.Binary Heap: a BH is a BT with following properties:
    - a BH is either Min Heap or Max Heap. In a Min Binary Heap, the key at root must be minimum among all keys present
    in BH. The same property must be recursively true for all nodes in BT.
    - it's a complete tree(all levels are completely filled except possibly the last level and the last level has all keys
    as left as possible). This property of BH makes them suitable to be stored in an array

2.Why a BH?
    - find the minimum or maximum number among a set of numbers in logN time.
    - we also want to make sure that inserting additional numbers does not take more than O(logN) time

3.Possible solutions:
    - store numbers in sorted array
    - store the numbers in LL in sorted manner
'''


class Heap:
    def __init__(self, size):
        self.custom_list = (size+1) * [None]
        self.heap_size = 0
        self.max_size = size + 1

# peek of heap = root of heap = returning custom_list[1]

def peek_of_heap(root_node):
    if not root_node:
        return
    else:
        return root_node.custom_list[1]

#size of heap = return number of filled cells

def size_of_heap(root_node):
    if not root_node:
        return
    else:
        return root_node.heap_size

#traversal of heap - level order traversal

def level_order_traversal_of_heap(root_node):
    if not root_node:
        return
    else:
        for i in range(1, root_node.heap_size+1):
            print(root_node.custom_list[i])


def heapify_tree_insert(root_node, index, heap_type):
    parent_index = int(index/2)
    if index <= 1:
        return
    if heap_type == 'Min':
        if root_node.custom_list[index] < root_node.custom_list[parent_index]:
            temp = root_node.custom_list[index]
            root_node.custom_list[index] = root_node.custom_list[parent_index]
            root_node.custom_list[parent_index] = temp
        heapify_tree_insert(root_node, parent_index, heap_type)
    elif heap_type == 'Max':
        if root_node.custom_list[index] > root_node.custom_list[parent_index]:
            temp = root_node.custom_list[index]
            root_node.custom_list[index] = root_node.custom_list[parent_index]
            root_node.custom_list[parent_index] = temp
        heapify_tree_insert(root_node, parent_index, heap_type)


def insert_node(root_node, node_value, heap_type):
    if root_node.heap_size + 1 == root_node.max_size:
        return 'The BH is full'
    root_node.custom_list[root_node.heap_size+1] = node_value
    root_node.heap_size += 1
    heapify_tree_insert(root_node, root_node.heap_size, heap_type)
    return 'The value has been successfully inserted'


def heapify_tree_extract(root_node, index, heap_type):
    left_index = index * 2
    right_index = index * 2 + 1
    swap_child = 0
    if root_node.heap_size < left_index:
        return
    elif root_node.heap_size == left_index:
        if heap_type == 'Min':
            if root_node.custom_list[index] > root_node.custom_list[left_index]:
                temp = root_node.custom_list[index]
                root_node.custom_list[left_index] = root_node.custom_list[left_index]
                root_node.custom_list[left_index] = temp
            return
        else:
            if root_node.custom_list[index] < root_node.custom_list[left_index]:
                temp = root_node.custom_list[index]
                root_node.custom_list[left_index] = root_node.custom_list[left_index]
                root_node.custom_list[left_index] = temp
            return
    else:
        if heap_type == 'Min':
            if root_node.custom_list[left_index] < root_node.custom_list[right_index]
                swap_child = left_index
            else:
                swap_child = right_index
            if root_node.custom_list[index] > root_node.custom_list[swap_child]:
                temp = root_node.custom_list[index]
                root_node.custom_list[left_index] = root_node.custom_list[swap_child]
                root_node.custom_list[swap_child] = temp
        else:
            if root_node.custom_list[left_index] > root_node.custom_list[right_index]
                swap_child = left_index
            else:
                swap_child = right_index
            if root_node.custom_list[index] < root_node.custom_list[swap_child]:
                temp = root_node.custom_list[index]
                root_node.custom_list[left_index] = root_node.custom_list[swap_child]
                root_node.custom_list[swap_child] = temp
        heapify_tree_insert(root_node, swap_child, heap_type)


def extract_node(root_node, heap_type):
    if root_node.heap_size == 0:
        return
    else:
        extracted_node = root_node.custom_list[1]
        root_node.custom_list[1] = root_node.custom_list[root_node.heap_size]
        root_node.custom_list[root_node.heap_size] = None
        root_node.heap_size -= 1
        heapify_tree_extract(root_node, 1, heap_type)
        return extracted_node

def delete_entire_heap(root_node):
    root_node.custom_list = None