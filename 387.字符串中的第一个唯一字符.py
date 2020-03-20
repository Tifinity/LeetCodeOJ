class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return -1
        re = [0 for i in range(26)]
        for i in range(len(s)):
            re[ord(s[i]) - 97] += 1
        for i in range(len(s)):
            if re[ord(s[i]) - 97] == 1:
                return i

        return -1

s=Solution()
print(s.firstUniqChar('loveleetcode'))