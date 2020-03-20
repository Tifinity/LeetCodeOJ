class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        res = h = ListNode(-1)
        while l1 and l2:
            if l1.val > l2.val:
                h.next = l2
                l2 = l2.next
            else:
                h.next = l1
                l1 = l1.next
            h = h.next
        if l1: h.next = l1
        if l2: h.next = l2
        return res.next
        