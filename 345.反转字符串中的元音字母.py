class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        yuan = ['a', 'i', 'u', 'e', 'o', 'A', 'E', 'I', 'O', 'U']
        i,j = 0, len(s)-1
        s = list(s)
        while i<j:
            print(i,j)
            if s[i] in yuan and s[j] in yuan:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            if s[i] not in yuan:
                i += 1
            if s[j] not in yuan:
                j -= 1
        return ''.join(s)
        
s = Solution()
print(s.reverseVowels('hello'))