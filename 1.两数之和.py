class Solution(object):
    def twoSum(self, nums, target):
        """
        一个哈希表记录已经遍历过的数
        """
        h = {}
        for k,v in enumerate(nums):
            if target - v in h:
                return [h[target - v], k]
            h[v] = k
        return []