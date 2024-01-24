'''
1.Trie:
    - a tree-based data structure that organizes information in a hierarchy
    1.1.Properties:
        - typically used to store or search strings in a space and time efficient way
        - any node in trie can store non-repetitive multiple characters
        - every node stores link of the next character of the string
        - every node keeps track of 'end of string'
    1.2.Why trie?
        - spelling checker
        - auto completion
'''

#TODO: can use this DS for spell checking search in next project
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_string = False

        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_string(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch) # by get function we check if the character already exists
            if node == None:
                node = TrieNode()
                current.children.update({ch: node})
            current = node
        current.end_of_string = TrieNode
        print('Successfully inserted')

    def search_string(self, word):
        current_node = self.root

        for i in word:
            node = current_node.children.get(i)
            if node == None:
                return False
            current_node = node

        if current_node.end_of_string == TrieNode:
            return True
        else:
            return False


def delete_string(index, root, word):
    ch = word[index]
    current_node = root.children.get(ch)
    can_this_node_be_deleted = False

    if len(current_node.children) > 1:
        delete_string(current_node, word, index+1)
        return False

    if index == len(word) - 1:
        if len(current_node.children) >= 1:
            current_node.end_of_string = False
            return False
        else:
            root.children.pop(ch)
            return True

    if current_node.end_of_string == TrieNode:
        delete_string(current_node, word, index+1)
        return False

    can_this_node_be_deleted = delete_string(current_node, word, index+1)
    if can_this_node_be_deleted == True:
        root.children.pop(ch)
        return True
    else:
        return False
