# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 双指针法，一起走总会遇到
        if not headA or not headB: return None
        ha, hb = headA, headB
        while ha is not hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA
        
        return None