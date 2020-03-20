class Solution(object):
    def toHex(self, num):
        if num == 0: return '0'
        res = ''
        mask = 15
        hexs = '0123456789abcdef'
        for i in range(8): 
            res = hexs[num & mask] + res
            num >>= 4
            print(num,res)
        return res.lstrip('0')

s= Solution()
print(s.toHex(-1))