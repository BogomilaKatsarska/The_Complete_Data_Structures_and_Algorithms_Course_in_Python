#1. Merge Two Sorted Linked Lists
class ListNode(object):
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.value <= l2.value:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        prev.next = l1 if l1 is not None else l2

        return prehead.next


class LinkedList:
    def __init__(self, value):
        new_node = ListNode(value)
        self.head = new_node
        self.tail = self.head
        self.length = 1

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

    def prepend(self, value):
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = ListNode(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


ll1 = LinkedList(0)
ll1.append(1)
ll1.append(2)
ll2 = LinkedList(0)
ll2.append(3)
solution = Solution()
print(solution.mergeTwoLists(ll1, ll2))