class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        滑动窗口法，找到一样的字符就删掉窗口最左边字符
        """
        if not s: return 0
        window = []
        maxlen = 0
        curlen = 0
        for i in range(len(s)):
            print(window)
            while s[i] in window:
                window.pop(0)
                curlen -= 1
            curlen += 1
            window.append(s[i])
            maxlen = curlen if curlen > maxlen else maxlen
        return maxlen

s = Solution()
a =  "pwwkew"
print(s.lengthOfLongestSubstring(a))