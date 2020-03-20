class Solution(object):
    def longestCommonPrefix(self, strs):
        # 垂直扫描法
        res = ''
        if not strs: return res
        for i in range(len(strs[0])):
            res += strs[0][i]
            for s in strs:
                if i == len(s) or s[i] != res[i]:
                    return res[:-1]
        return res

    def longestCommonPrefix(self, strs):
        # 水平扫描法
        if len(strs) == 0: return ''
        res = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(res) != 0:
                res = res[:-1]
        return res

s= Solution()
a = ["aa", "a"]
print(s.longestCommonPrefix(a))