class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "":
            return ""
        s = s.strip()
        strs = s.split(' ')
        #print(strs)
        res = []
        for st in strs:
            if st == '':
                continue
            st += ' '
            res.insert(0, st)
        return ''.join(res).strip()
s = Solution()
str1 = "the sky is blue"
str2 = "  hello world!  "
str3 = "a good   example"
print(s.reverseWords(str1))
print(s.reverseWords(str2))
print(s.reverseWords(str3))