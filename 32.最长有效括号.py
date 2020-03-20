class Solution(object):
    def longestValidParentheses(self, s):
        # 栈的top记录了start，长度就是i - start
        res = 0
        m = []
        m.append(-1)
        for i in range(len(s)):
            if s[i] == '(':
                m.append(i)
            else:
                m.pop()
                if not m:
                    m.append(i)
                else:
                    res = max(res, i - m[-1])
        return res 

    def longestValidParentheses1(self, s):
        # 用两个变量保存左括号和右括号的数量
        if len(s) == 0: return 0
        res = 0
        left = right = 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            if s[i] == ')':
                right += 1
            if left == right:
                res = max(res, 2*left)
            if left < right:
                left = 0
                right = 0
        left = right = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == ')':
                left += 1
            if s[i] == '(':
                right += 1
            if left == right:
                res = max(res, 2*left)
            if left < right:
                left = 0
                right = 0
        return res 

s = Solution()
print(s.longestValidParentheses1(')()())()()()'))