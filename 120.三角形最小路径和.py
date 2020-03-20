class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """


t = [
        [2],
        [3,4],
        [6,5,7],
        [4,1,8,3]
    ]
s = Solution()
print(s.minimumTotal(t))