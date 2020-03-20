# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        # 迭代
        if not head or not head.next: return head
        h1 = h3 = head
        h2 = head.next
        head = ListNode(-1)
        head.next = h2
        while h1 and h2:
            h1.next = h2.next
            h2.next = h1
            h3 = h1
            h1 = h1.next
            h2 = h1.next if h1 else None
            if h2:
                h3.next = h2
        return head.next

    def swapPairs(self, head: ListNode) -> ListNode:
        # 递归
        if not head or not head.next: return head
        first_node = head
        second_node = head.next
        first_node.next  = self.swapPairs(second_node.next)
        second_node.next = first_node
        return second_node