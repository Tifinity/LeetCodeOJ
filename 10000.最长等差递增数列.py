class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0

        d = 0
        res = 1
        now = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] <= 0:
                continue
            if d == nums[i] - nums[i-1]:
                now += 1
            else:
                now = 2
            res = max(res, now)
            d = nums[i] - nums[i-1]
        return res