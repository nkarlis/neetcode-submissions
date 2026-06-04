class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions =[[1, 0], [-1, 0], [0, 1], [0, -1]]
        visit = set()

        def dfs(r, c):
            if(r not in range(ROWS) or c not in range(COLS) or grid[r][c] == 0 or 
            (r,c) in visit):
                return 0

            visit.add((r,c))
            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c-1) + dfs(r, c+1)
            


        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):  
                if (r,c) not in visit and grid[r][c]!=0:
                    maxArea = max(dfs(r,c), maxArea)

        return maxArea

