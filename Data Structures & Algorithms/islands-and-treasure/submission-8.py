class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
        def dfs(r, c):
            if(r not in range(ROWS) or c not in range(COLS)
            or (r, c) in visit or grid[r][c] == -1):
                return
            q.append([r, c])
            visit.add((r, c))
        time = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = time
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
            time += 1

        