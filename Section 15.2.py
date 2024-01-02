class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def remove_elements(self, head, val):
        dummy_head = ListNode(-1)
        dummy_head.next = head

        prev_node, curr_node = dummy_head, head
        while curr_node:
            if curr_node.val == val:
                prev_node.next = curr_node.next

            else:
                prev_node = curr_node
            curr_node = curr_node.next

        return dummy_head.next