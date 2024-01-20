'''
1.BST: a binary tree with additional properties:
    - in the left subtree the value of a node is less than or equal to its parent node's value
    - in the right subtree the value of a node is greater than its parent node's value

2.Why BST?
    - performs faster than BT when inserting and deleting nodes
'''


class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def insert_node(root_node, node_value):
    if root_node.data is None:
        root_node.data = node_value
    elif node_value <= root_node.data:
        if root_node.left_child is None:
            root_node.left_child = BinarySearchTreeNode(node_value)
        else:
            insert_node(root_node.left_child, node_value)
    else:
        if root_node.right_child is None:
            root_node.right_child = BinarySearchTreeNode(node_value)
        else:
            insert_node(root_node.right_child, node_value)
        return 'The node has been successfully inserted'


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

#DELETE NODE STARTS HERE


def min_value_node(bst_node):
    current = bst_node
    while current.left_child is not None:
        current = current.left_child
    return current


def delete_node(root_node, node_value):
    if root_node is None:
        return root_node
    if node_value < root_node.data:
        root_node.left_child = delete_node(root_node.left_child, node_value)
    elif node_value > root_node.data:
        root_node.right_child = delete_node(root_node.right_child, node_value)
    else:
        if root_node.left_child is None:
            temp_node = root_node.right_child
            root_node = None
            return temp_node

        if root_node.right_child is None:
            temp_node = root_node.left_child
            root_node = None
            return temp_node

        temp_node = min_value_node(root_node.right_child)
        root_node.data = temp_node.data
        root_node.right_child = delete_node(root_node.right_child, temp_node.data)
    return root_node


def delete_BST(root_node):
    root_node.data = None
    root_node.left_child = None
    root_node.right_child = None
    return 'The BST has been successfully deleted'