class Solution(object):
    def preorderTraversal(self, root):
        stack = [root]
        res = []
        if not root: return res
        while len(stack) != 0:
            tmp = stack.pop()
            res.append(tmp.val)
            if tmp.right:
                stack.append(tmp.right)
            if tmp.left:
                stack.append(tmp.left)
        return res