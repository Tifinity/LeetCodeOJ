class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        from collections import Counter
        m = Counter(magazine)
        for i in ransomNote:
            if i not in m:
                return False
            else:
                if m[i] == 1:
                    del m[i]
                else:
                    m[i] -= 1
            #print(m)
        return True

s = Solution()
print(s.canConstruct("a", "b"))
print(s.canConstruct("aa", "ab"))
print(s.canConstruct("aa", "aab"))