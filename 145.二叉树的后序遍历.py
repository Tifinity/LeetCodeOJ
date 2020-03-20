class Solution(object):
    def postorderTraversal(self, root):
        if not root: return []
        res = []
        stack = [root]
        visit = set()
        while len(stack) != 0:     
            tmp = stack[-1]
            lv = rv = True
            if tmp.right and tmp.right not in visit:
                rv = False
                stack.append(tmp.right)
            if tmp.left and tmp.left not in visit:
                lv = False
                stack.append(tmp.left)
            if lv and rv:
                res.append(tmp.val)
                visit.add(tmp)
                stack.pop()
        return res