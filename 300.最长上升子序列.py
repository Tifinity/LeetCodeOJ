def lengthOfLIS(nums):
    '''
    给定一个无序的整数数组，找到其中最长上升子序列的长度。
    输入: [10,9,2,5,3,7,101,18]
    输出: 4 
    解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
    '''
    # 动态规划
    dp = [0 for i in range(len(nums))]
    dp[0] = 1
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp[n]
        
print(lengthOfLIS([10,9,2,5,3,7,101,18]))
        
