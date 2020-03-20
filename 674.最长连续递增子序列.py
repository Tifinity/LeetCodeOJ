class Solution(object):
    def findLengthOfLCIS(self, nums):
        # 给定一个未经排序的整数数组，找到最长且连续的的递增序列
        '''
        输入: [1,3,5,4,7]
        输出: 3
        解释: 最长连续递增序列是 [1,3,5], 长度为3。
        尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，
        因为5和7在原数组里被4隔开。 
        '''
        if not nums: return 0
        res = 1
        now = 1
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                now = 1
            else:
                now += 1
            res = max(res, now)
        return res  