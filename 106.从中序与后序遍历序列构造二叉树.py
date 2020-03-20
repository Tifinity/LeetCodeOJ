class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        if not inorder: return None
        root = TreeNode(postorder[-1])
        #print(root.val)
        i = inorder.index(root.val)
        root.left = self.buildTree(inorder[:i], postorder[:i])
        root.right = self.buildTree(inorder[i+1:], postorder[i:-1])
        return root

s = Solution()
a = s.buildTree([9,3,15,20,7], [9,15,7,20,3])

