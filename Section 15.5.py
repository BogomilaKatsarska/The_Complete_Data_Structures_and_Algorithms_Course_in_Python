class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def middle_node(self, head):

        fast = head
        while fast and fast.next:
            head = head.next
            fast = fast.next.next

        return head

