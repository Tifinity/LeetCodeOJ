class Solution:
    def threeSum(self, nums):
        # 先排序，再去重
        if nums == [] or len(nums) < 3:
            return []
        nums.sort()
        res = []

        for i in range(len(nums)):
            if nums[i] > 0: return res 
            if i>0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left<right:
                # 等于0加入结果，并且左右分别跳过相等的值
                if nums[i]+nums[left]+nums[right]==0:
                    res.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left = left+1
                    while left<right and nums[right]==nums[right-1]:
                        right = right-1
                    left = left+1
                    right = right-1
                # 大于0则右边减
                elif nums[i]+nums[left]+nums[right]>0:
                    right = right-1
                # 小于0则左边加
                else:
                    left = left+1
        return res

nums = [-2,0,1,1,2]
s = Solution()
print(s.threeSum(nums))