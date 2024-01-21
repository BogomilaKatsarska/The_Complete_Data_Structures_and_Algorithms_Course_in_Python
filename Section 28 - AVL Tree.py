'''
1.AVL Tree: an AVL tree is a self-balancing BST where the difference between heights of left and right
            subtrees cannot be more than one for all nodes

            - if at any time heights of left and right subtrees differ by more than one, then rebalancing
            is done to restore AVL property which is called ROTATION

            - WHY AVL Tree?: decrease time complexity - much faster # O log n
'''


class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 1


def preorder_traversal(root_node):
    if not root_node:
        return
    print(root_node)
    preorder_traversal(root_node.left_child)
    preorder_traversal(root_node.right_child)


def inorder_traversal(root_node):
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
        while not custom_queue.is_empty():
            root = custom_queue.dequeue()
            print(root.value.data)
            if root.value.left_child is not None:
                custom_queue.enqueue(root.value.left_child)
            if root.value.right_child is not None:
                custom_queue.enqueue(root.value.right_child)


def search_node(root_node, node_value):
    if root_node.data == node_value:
        print('The value is found')
    elif node_value < root_node.data:
        if root_node.left_child.data == node_value:
            print('The value is found')
        else:
            search_node(root_node.left_child, node_value)
    else:
        if root_node.right_child.data == node_value:
            print('The value is found')
        else:
            search_node(root_node.right_child, node_value)

