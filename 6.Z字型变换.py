class Solution(object):
    def convert(self, s, numRows):
        """
        直接模拟，n列的字符串数组
        """
        if numRows == 1: return s
        buf = ['' for _ in range(numRows)]
        flag = -1
        row = 0
        for ch in s:
            buf[row] += ch
            if row == 0 or row == numRows-1: flag *= -1
            row += flag
        res = ''
        for string in buf:
            res += string
        return res