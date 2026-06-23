class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        dire = [[1, 0], [-1, 0], [0, 1], [0,-1]]
        visit = set()
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visit.add((r, c))
                    q.append((r, c))
        def dfs(r, c):
            if( r not in range(ROWS) or c not in range(COLS)
            or (r, c) in visit or grid[r][c] == -1):
                return
            visit.add((r,c))
            q.append((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
            dist +=1
        
