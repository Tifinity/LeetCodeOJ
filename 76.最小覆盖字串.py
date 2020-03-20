class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # 困难，滑动窗口，很多细节
        from collections import Counter
        if not s or not t or len(s)<len(t):
            return ''
        need = Counter(t)
        window = Counter()
        left = 0
        right = 0
        st = 0
        res = 2147483647
        cnt = 0
        while right < len(s):
            tmp = s[right]
            if tmp in need:
                window[tmp] += 1
                if window[tmp] == need[tmp]:
                    cnt += 1
            print(cnt, left, right, need, window) 
            while cnt == len(need):
                if right - left + 1 < res:
                    st = left
                    res = right - left + 1 
                res = min(res, right - left + 1)
                tmp2 = s[left]
                if tmp2 in need:
                    window[tmp2] -= 1
                    if window[tmp2] < need[tmp2]:
                        cnt -= 1
                print(tmp2, window)
                left += 1
            right += 1   
        print(st, res)      
        return s[st: st+res] if res != 2147483647 else ''

S = "aa"
T = "aa"
s = Solution()
print(s.minWindow(S, T))