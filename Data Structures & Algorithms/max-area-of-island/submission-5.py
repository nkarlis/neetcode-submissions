class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        visit = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    q.append((r,c))


        def dfs(r,c):
            if((r,c) in visit or r not in range(ROWS) 
            or c not in range(COLS) or grid[r][c] == 0):
                return 0

            visit.add((r,c))
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)

        maxArea = 0
        for i in range(len(q)):
            r, c = q.popleft()
            if (r, c) not in visit:
                area = dfs(r,c)
                maxArea = max(maxArea, area)
        return maxArea