class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))

        def addCell(r, c):
            if(r not in range(ROWS) or c not in range(COLS) or
                (r, c) in visit or grid[r][c] == -1):
                return
            q.append((r,c))
            visit.add((r,c))

        dist = 0
        while q:
            for i in range(len(q)):
                (r, c) = q.popleft()
                addCell(r+1, c)
                addCell(r-1, c)
                addCell(r, c+1)
                addCell(r, c-1)
                grid[r][c] = dist
            dist += 1