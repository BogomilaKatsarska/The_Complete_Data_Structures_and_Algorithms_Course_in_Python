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