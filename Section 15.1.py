class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def delete_duplicates(self, head):
        if not head:
            return None

        seen = set()
        dummy = ListNode(-1)
        dummy.next = head
        prev_node = dummy
        current_node = head

        while current_node:
            if current_node.val in seen:
                prev_node.next = current_node.next
                current_node = current_node.next

            else:
                seen.add(current_node.val)
                prev_node = current_node
                current_node = current_node.next

            return dummy.next

