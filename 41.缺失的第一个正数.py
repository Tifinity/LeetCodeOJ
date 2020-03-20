class Solution(object):
    def firstMissingPositive(self, nums):
        if not nums: return 1
        # 缺的第一个不可能是大于 nums长度的
        for i in range(len(nums)):
            if nums[i] < 0 or nums[i] > len(nums):
                nums[i] = 0
        # 找到最大的数，建立一个哈希表
        m = max(nums)
        arr = [0 for i in range(m + 1)]
        for i in nums:
            arr[i] = 1
        # 找到哈希表中的第一个0，即结果，否则是m+1
        for j in range(1, len(arr)):
            if arr[j] == 0:
                return j 
        return m + 1

s = Solution()
print(s.firstMissingPositive([3,4,-1,1]))