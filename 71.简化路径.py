class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # 先左右去掉/，再按/拆分
        stack = []
        path = path.strip('/')
        path = path.split('/')
        # 对每一个子路径，三种情况
        for p in path:
            # 直接跳过
            if p == '' or p == '.':
                continue
            # 上一个
            elif p == '..':
                if stack != []:
                    stack.pop()
            # 下一个
            else:
                stack.append(p)
        return '/' + '/'.join(stack)

s= Solution()
s1 = "/home/"
s2 = "/../"
s3 = "/home//foo/"
s4 = "/a/./b/../../c/"
s5 = "/a/../../b/../c//.//"
s6 = "/a//b////c/d//././/.."
#print(s.simplifyPath(s1))
#print(s.simplifyPath(s2))
#print(s.simplifyPath(s3))
print(s.simplifyPath(s4))
print(s.simplifyPath(s5))
