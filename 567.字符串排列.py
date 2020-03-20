from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2): return False
        s1map = Counter(s1)
        s2map = Counter(s2[:len(s1)])
        if s1map == s2map: return True
        print(s1map, s2map)
        i = 0
        j = len(s1)-1
        while j < len(s2)-1:
            s2map[s2[i]] -= 1
            if s2map[s2[i]] == 0:
                del s2map[s2[i]]
            j += 1
            s2map[s2[j]] += 1
            print(s1map,s2map)
            if s1map == s2map:
                return True
            i += 1
            
        return False

s= Solution()
s1 = "ab"
s2 = "eidboaoo"
print(s.checkInclusion(s1, s2))