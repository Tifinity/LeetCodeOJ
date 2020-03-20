class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        s1 = set(arr)
        s2 = [1001 for i in range(3000)]
        for n in arr:
            if s2[n] == 1001:
                s2[n] -= 1001
            s2[n] += 1
        s2 = set(s2)
        s1.add(1001)
        print(s1,s2)
        return len(s1) == len(s2)

    def uniqueOccurrences1(self, arr):
        from collections import Counter
        c = Counter(arr)
        v = c.values()
        print(c)
        return len(v) == len(set(v))

    def uniqueOccurrences2(self, arr):
        d = {}
        for i in arr:
            if i not in d:
                d.update({i:1})
            else:
                d[i] += 1
        print(d)
        return len(d.values()) == len(set(d.values()))
                

s = Solution()
print(s.uniqueOccurrences1( [-3,0,1,-3,1,1,1,-3,10,0]))