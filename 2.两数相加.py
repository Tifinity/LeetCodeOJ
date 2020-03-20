# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # 链表加法
        if not l1: return l2
        if not l2: return l1
        carry = 0
        res = head = ListNode(-1)
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            tmp = x + y + carry
            carry = tmp // 10
            head.next = ListNode(tmp % 10)
            head = head.next
            if l1: l1 = l1.next 
            if l2: l2 = l2.next
        if carry:
            head.next = ListNode(carry)
        return res.next

def printlist(node):
    while node:
        print(node.val)
        node = node.next

n1 = ListNode(2)
n2 = ListNode(7)
n3 = ListNode(9)
n1.next = n2
n2.next = n3

n4 = ListNode(2)
n5 = ListNode(8)
n4.next = n5

s = Solution()
printlist(s.addTwoNumbers(n1, n4))