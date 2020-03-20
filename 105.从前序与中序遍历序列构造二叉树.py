class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder:
        	return None

        root = TreeNode(preorder[0])
        #print(root.val)
        i = inorder.index(root.val)
       	root.left = self.buildTree(preorder[1:i+1], inorder[:i])
       	root.right = self.buildTree(preorder[i+1:], inorder[i+1:])

       	return root

s = Solution()
a = s.buildTree([3,9,20,15,7], [9,3,15,20,7])