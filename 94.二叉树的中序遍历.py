class Solution(object):
    def inorderTraversal(self, root):
        if not root: return []
        res = []
        stack = []
        tmp = root
        while tmp != None or len(stack) != 0:
            while tmp:
                stack.append(tmp)
                tmp = tmp.left  
            tmp = stack.pop()
            res.append(tmp.val)
            tmp = tmp.right
        return res