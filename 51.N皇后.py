class Solution(object):
    def solveNQueens(self, n):
        import copy
        res = []
        board = [['.' for i in range(n)] for j in range(n)]

        def back(row):
            if row == n:
                res.append(copy.deepcopy(board))
                return
            for col in range(n): 
                if check(row, col):
                    board[row][col] = 'Q'
                    back(row+1)
                    board[row][col] = '.'
                
        def check(row, col):
            for i in range(row):
                for j in range(n):
                    if board[i][j] == 'Q' and (j==col or abs(row-i)==abs(col-j)):
                        return False
            return True

        back(0)

        real_res = []
        for _res in res:
            tmp_board = []
            for row in _res:
                tmp = ''
                for s in row:
                    tmp += s 
                tmp_board.append(tmp)
            real_res.append(tmp_board)
        return real_res
s = Solution()
print(s.solveNQueens(4))