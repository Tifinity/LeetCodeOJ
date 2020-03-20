# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        # 双指针法，用哑节点处理一下边界情况
        res = ListNode(-1)
        res.next = head
        fast = slow = res
        while n + 1 > 0:
            n -= 1
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return res.next