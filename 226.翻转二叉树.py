class TreeNode(object):
	def __init__(self, x):
	    self.val = x
	    self.left = None
	    self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

s = Solution()

a = TreeNode(4)
b = TreeNode(2)
c = TreeNode(7)
d = TreeNode(1)
e = TreeNode(3)
f = TreeNode(6)
g = TreeNode(9)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

