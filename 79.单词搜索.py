class Solution(object):
    directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # 回溯
        h = len(board)
        if h == 0: return False
        w = len(board[0])
        visit = [[False for _ in range(w)] for _ in range(h)]

        def back(x, y, word):
            if len(word) == 0: return True
            if 0 <= x < h and 0 <= y < w and \
                board[x][y] == word[0] and not visit[x][y]:
                visit[x][y] = True
                for direct in self.directs:
                    next_x = x + direct[0]
                    next_y = y + direct[1]
                    if back(next_x, next_y, word[1:]):
                        return True
                visit[x][y] = False
            return False

        for i in range(h):
            for j in range(w):
                if back(i, j, word):
                    return True
        return False

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED"

s = Solution()
print(s.exist(board, word))