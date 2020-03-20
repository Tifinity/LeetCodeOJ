# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 双指针法，快慢指针
        if not head: return None
        if not head.next: return None
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                break
        if fast is not slow: return None     
        p = head
        q = fast
        while p is not q:
            p = p.next
            q = q.next
        return p

