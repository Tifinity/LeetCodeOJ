class Solution(object):
    def spiralOrder(self, matrix):
        # 使用zip，每拿一行，逆时针旋转矩阵
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(map(list, zip(*matrix)))[::-1]
        return res

a = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12]
    ]
s = Solution()
print (s.spiralOrder(a))