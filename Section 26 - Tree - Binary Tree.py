'''
1. Tree: non-linear data structure with hierarchical relationships between its elements without having any cycle,
        it is basically reversed fromm a real life tree
        - represents hierarchical data
        - each node has two components: data and a link to its sub-category
        - base category and sub-categories under it

        - allow quicker and easier access to the data
        - store hierarchical data, like folder structure, organization structure, XML/HTML data

2. Terminology:
        - root: top node without parent
        - edge: a link between parent and child
        - leaf: a node which does not have children
        - sibling: a children of same parent
        - ancestor: parent, grandparent, great-grandparent of a node
        - depth of node: a length of the path from root to node
        - height of node: a length of the path from the node to the deepest node
        - depth of tree: depth of root node
        - height of tree: height of root node

3. Binary Tree: data structures in which each node has at most 2 children, ofter referred as the left and right children
        - binary tree is a family of data structure(BST, Heap tree, red black trees, syntax tree)

4.Types of binary tree:
        - Full BT: each node has either 2children or 0children
        - Perfect BT: all non-leaf nodes have 2children and they are at the same depth
        - Complete BT: all levels are perfect except the last one(not completely filled)
        - Balanced BT: all leaf nodes are located in the same distance from the root node

5.Binary Tree Repr:
        Root index: 1
        Left child: cell[2x] => 2
        Right child: cell[2x+1] => 3

6.Traversal:
        6.1.Depth First Search:
            - preorder traversal
                Root Node -> Left Subtree -> Right Subtree
            - inorder traversal
                Left Subtree -> Root Node -> Right Subtree
            - post order traversal
                Left Subtree -> Right Subtree -> Root Node
        6.2.Breadth First Search:
            - level order traversal
                We visit level by level
'''
import queue

'''
class TreeNode:
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        res = " "*level + str(self.data) + "\n"
        for child in self.children:
            res += child.__str__(level+1)
        return res

    def add_child(self, tree_node):
        self.children.append(tree_node)


tree = TreeNode('Drinks', [])
cold = TreeNode('Cold', [])
hot = TreeNode('Hot', [])
tree.add_child(cold)
tree.add_child(hot)
tea = TreeNode('Tea', [])
coffee = TreeNode('Coffee', [])
cola = TreeNode('Cola', [])
fanta = TreeNode('Fanta', [])
cold.add_child(cola)
cold.add_child(fanta)
hot.add_child(tea)
hot.add_child(coffee)
print(tree)
'''

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def preorder_traversal(root_node): #O(n)
    if not root_node:
        return
    print(root_node.data)
    preorder_traversal(root_node.left_child)
    preorder_traversal(root_node.right_child)


def inorder_traversal(root_node): #O(n)
    if not root_node:
        return
    inorder_traversal(root_node.left_child)
    print(root_node.data)
    inorder_traversal(root_node.right_child)


def postorder_traversal(root_node):
    if not root_node:
        return
    postorder_traversal(root_node.left_child)
    postorder_traversal(root_node.right_child)
    print(root_node.data)


def level_order_traversal(root_node):
    if not root_node:
        return
    else:
        custom_queue = queue.Queue()
        custom_queue.enqueue(root_node)
        while not(custom_queue.is_empty()):
            root = custom_queue.dequeue()
            print(root.value.data)
            if root.value.left_child is not None:
                custom_queue.enqueue(root.value.left_child)
            if root.value.right_child is not None:
                custom_queue.enqueue(root.value.right_child)


# we will use level order traversal because it uses queue which performs better than stack
def search_binary_tree(root_node, node_value):
    if not root_node:
        return 'The binary tree doe not exist'
    else:
        custom_queue = queue.Queue()
        custom_queue.enqueue(root_node)
        while not custom_queue.is_empty:
            root = custom_queue.dequeue()
            if root.value.data == node_value:
                return 'Success: This node exists in the BT'
            if root.value.left_child is not None:
                custom_queue.enqueue(root.value.left_child)
            if root.value.right_child is not None:
                custom_queue.enqueue(root.value.right_child)
        return 'The value does not exist in the BT'


def insert_node_BT(root_node, new_node):
    if not root_node:
        root_node = new_node
    else:
        custom_queue = queue.Queue()
        custom_queue.enqueue(root_node)
        while not(custom_queue.is_empty()):
            root = custom_queue.dequeue()
            if root.value.left_child is not None:
                custom_queue.enqueue(root.value.left_child)
            else:
                root.value.left_child = new_node
                return 'Successfully inserted node'
            if root.value.right_child is not None:
                custom_queue.enqueue(root.value.right_child)
            else:
                root.value.right_child = new_node
                return 'Successfully inserted node'


#DELETE A NODE BEWLOW

def get_deepest_node(root_node):
    if not root_node:
        return
    else:
        custom_queue = queue.Queue()
        custom_queue.enqueue(root_node)
        while not custom_queue.is_empty():
            root = custom_queue.dequeue()
            if root.value.left_child is not None:
                custom_queue.enqueue(root.value.left_child)
            if root.value.right_child is not None:
                custom_queue.enqueue(root.value.right_child)
        deepest_node = root.value
        return deepest_node


def delete_deepest_node(root_node, deepest_node):
    if not root_node:
        return
    else:
        custom_queue = queue.Queue()
        custom_queue.enqueue(root_node)
        while not custom_queue.is_empty():
            root = custom_queue.dequeue()
            if root.value is deepest_node:
                root.value = None
                return
            if root.value.right_child:
                if root.value.right_child is deepest_node:
                    root.value.right_child = None
                    return
                else:
                    custom_queue.enqueue(root.value.right_child)
            if root.value.left_child:
                if root.value.left_child is deepest_node:
                    root.value.left_child = None
                    return
                else:
                    custom_queue.enqueue(root.value.left_child)


def delete_node_BT(root_node, node_to_be_deleted):
    if not root_node:
        return 'The BT does not exist'
    else:
        custom_queue = queue.Queue()
        custom_queue.enqueue(root_node)
        while not custom_queue.is_empty():
            root = custom_queue.dequeue()
            if root.value.data == node_to_be_deleted:
                deepest_node = get_deepest_node(root_node)
                root.value.data = deepest_node.data
                delete_deepest_node(root_node, deepest_node)
                return 'The node has been successfully deleted'
            if root.value.left_child is not None:
                custom_queue.enqueue(root.value.left_child)
            if root.value.right_child is not None:
                custom_queue.enqueue(root.value.right_child)
        return 'Failed to delete'


def delete_BT(root_node):
    if not root_node:
        return 'The BT does not exist'
    else:
        root_node.data = None
        root_node.left_child = None
        root_node.right_child = None
        return 'The BT has been successfully deleted'