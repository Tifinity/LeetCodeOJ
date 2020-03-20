class Solution(object):
    def isValid(self, s):
        """
        用栈
        如果括号只有一种，用一个变量就可以优化空间
        """
        stack = []
        left = ['(', '[', '{']
        right = [')', ']', '}']
        for i in range(len(s)):
            if s[i] in left:
                stack.append(s[i])
            if s[i] in right:
                if not stack: return False
                tmp = stack.pop()
                l = left.index(tmp)
                r = right.index(s[i])
                if l != r: return False        
        if len(stack) == 0: return True
        return False
s= Solution()
print(s.isValid("]"))