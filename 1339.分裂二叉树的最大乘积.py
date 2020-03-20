class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        list_sum = []
        rootsum = rootSum(root, list_sum)
        res = 0
        for s in list_sum:
            res = max(res, s * (rootsum - s))
        return res % ( 10**9 + 7 )

    def rootSum(self, root, list_sum):
        if root == None:
            return 0
        sum = root.val + self.rootSum(root.left, list_sum) + self.rootSum(root.right, list_sum)
        list_sum.append(sum)
        return sum

    