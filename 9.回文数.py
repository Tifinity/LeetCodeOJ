class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        re = 0
        n = x
        while x // 10:
            re = re*10 + x%10
            x = x // 10
        re = re*10 + x%10
        if re == n: return True
        return False