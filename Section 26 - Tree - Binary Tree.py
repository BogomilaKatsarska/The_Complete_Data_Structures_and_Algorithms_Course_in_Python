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