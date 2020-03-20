class Solution:
    def reverse(self, x: int) -> int:
        flag = 1 if x > 0 else -1
        x = abs(x)
        res = 0
        while x // 10:
            res = res * 10 + x % 10
            x = x // 10
        res = res * 10 + x % 10
        if -res < -2**31 or res > 2**31 - 1:
            return 0
        return res * flag 
        
s = Solution()
print(s.reverse(-14236469))