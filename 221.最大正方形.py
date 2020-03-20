class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row = len(matrix) 
        if row == 0: return 0
        col = len(matrix[0])
        if col == 0: return 0
        dp = [[0 for i in range(col+1)] for i in range(row+1)]
        print(dp)
        print(matrix)
        res = 0
        for i in range(1, row+1):
            for j in range(1, col+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                    res = max(res, dp[i][j])
        return res**2

s = Solution()
a = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]
b = []
print(s.maximalSquare(b))