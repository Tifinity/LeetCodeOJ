class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        if not grid or not grid[0]: return 0
        visit = set()
        res = 0

        def dfs(x, y):
            if (x,y) in visit or not 0<=x<len(grid) or not 0<=y<len(grid[0]) or grid[x][y] == 0:
                return 0
            visit.add((x, y))
            return (1 + dfs(x-1, y) + dfs(x+1, y) + 
                    dfs(x, y-1) + dfs(x, y+1))

        return max(dfs(x, y) 
                for x in range(len(grid)) 
                for y in range(len(grid[0])))

s = Solution()
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(s.maxAreaOfIsland(grid))