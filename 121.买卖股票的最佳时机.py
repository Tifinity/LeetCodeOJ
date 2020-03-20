class Solution(object):
    def maxProfit(self, prices):
        diff = []
        for i in range(1, len(prices)):
            diff.append(prices[i] - prices[i-1])
        res = 0
        today = 0
        for j in diff:
            today = max(today, today+j)
            res = max(res, today)
        return res

    def maxProfit_dp(self, prices):
        dp = []
        for i in range(len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], -prices[i])

s = Solution()
print(s.maxProfit([7,6,4,3,1]))