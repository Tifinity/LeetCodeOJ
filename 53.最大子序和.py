class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = max_now = nums[0]
        for n in nums[1:]:        
            max_now = max(n, max_now + n)
            res = max(res, max_now)
        return res