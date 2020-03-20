# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if not root: return []
        queue = [root, None]
        level = []
        res = []
        flag = True
        while len(queue) > 0:
            node = queue.pop(0)
            if node:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if flag:
                    level.append(node.val)
                else:
                    level.insert(0, node.val)
            else:
                if len(queue) > 0:
                    queue.append(None)
                res.append(level)
                level = []
                flag = not flag
        return res


tree = TreeNode(3)
tree1 = TreeNode(9)
tree2 = TreeNode(20)
tree3 = TreeNode(15)
tree4 = TreeNode(7)

tree.left = tree1
tree.right = tree2
tree2.left = tree3
tree2.right = tree4

s = Solution()
print(s.zigzagLevelOrder(tree))



