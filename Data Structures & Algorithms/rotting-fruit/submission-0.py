class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()

        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r, c])
                if grid[r][c] == 1:
                    fresh+=1

        def addCell(r, c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == 0 or grid[r][c]  == 2:
                return
            nonlocal fresh
            fresh -=1
            q.append([r, c])
            grid[r][c] = 2


        total = 0

        while q and fresh>0:
            for i in range(len(q)):
                r, c = q.popleft()
                addCell(r+1, c)
                addCell(r-1, c)
                addCell(r, c+1)
                addCell(r, c-1)
            total +=1

        return total if fresh == 0 else -1
