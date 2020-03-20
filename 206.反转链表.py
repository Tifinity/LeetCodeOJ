
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        res = None
        
        while head:
            tmp = ListNode(head.val)
            tmp.next = res
            res = tmp
            head = head.next
        
        return res
