# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        中序遍历递增 + 比较每个节点与上一个节点的值
        """
        if not root: return True
        pre = float('-inf')
        stack = []
        tmp = root
        while stack or tmp:
            while tmp:
                stack.append(tmp)
                tmp = tmp.left
            tmp = stack.pop()
            if tmp.val <= pre:
                return False
            pre = tmp.val
            tmp = tmp.right
        return True